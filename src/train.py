# imports
import json
import torch
import torch.nn as nn
from nltkproperties import tokenize, stem, bag_of_words, show_part_of_speech, synonym_recognition
import numpy as np
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet
import shutil




# open the json file and load the data and get tags, patterns
with open('intents.json', encoding='utf-8') as i:
    # load contents of json file into intents
    intents = json.load(i)
    
        
# for every intent in intents note: there are around 39 intnets before merging with main
for  (patternindex,intent) in enumerate( intents['intents'], start = 1):
    # keeps track of what was in 'patterns' before
    previouslist = intent['patterns']
    # for every sentence in patterns
    for pattern in intent['patterns']:
        # print sentence
        print("Sentence" ,pattern)
        # print index of the sentence. If its in first intent it will be 1 and if its in second intent it will be 2
        print("Index",patternindex)

        #method to bring set of every word and parts of speech according to every word
        patter_list_sentence = show_part_of_speech(pattern)
        # temp variables to be used for future
        # list of new sentences that we will be creating with synonyms
        newsentencelist = []
        newpattern= []
        currentpattern = []
        totalpattern = []

        # proof that part of speech works
        for i in patter_list_sentence:
            # for every word print word
            print("Word: " ,i[0])
            # for every word print what it is
            print("Tag:",i[1])
            # new sentence 
            newsentence = ""
            
            # if part of speech is 'JJ' which means if its adjective
            if i[1] == 'JJ': 
                # find synonyms for the word.
                synonyms = synonym_recognition(i[0])
                # sort the synonyms. Ex: word great has synonyms good, amazing, awesome, good. We dont want 2 'good' here
                synonyms = sorted(set(synonyms))

                # print the set for the proof
                print("Synonyms for the word is: ",synonyms)
                
                # for every sentence in synonyms
                for synonym in synonyms:
                    # replace that word in pattern with the synonym and put it in new sentence
                    newsentence = pattern.replace(i[0], synonym)

                    # printing new sentence showing that sentence has changed. If it was I feel good, it will now become I feel great
                    print("New sentences: ", newsentence)
                    
                    # append this new sentence to the newsentence list
                    newsentencelist.append(newsentence)

                    # what sentences are currently in 'patterns'
                    currentpattern = intent["patterns"];
                    print("Before adding new synonyms: ", currentpattern)
                    newpattern = newsentencelist

                    # add new list with old responses and new sentences so we get more pattern
                    totalpattern = currentpattern + newpattern
        # save it in the actual intents    
        intent["patterns"] = totalpattern + previouslist  
        # print in the console to prove that there is now new list with sentences that contain synonyms
        print("Total Pattern", intent["patterns"])
    
        


all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize method from nltk_utils class
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

# words to ignore
ignore_words = ['?', '!', '.', ',']
# stemming all_words except ignored words
all_words = [stem(w) for w in all_words if w not in ignore_words]
# since set has unique elements in it putting them
# in a set and sorting makes unique sorted elements
all_words = sorted(set(all_words))
tags = sorted(set(tags))


# training data
X_train = []
Y_train = []

for(pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)

    Y_train.append(label)

X_train = np.array(X_train)
Y_train = np.array(Y_train)

# chatdataset class


class ChatDataSet(Dataset):
    # init funciton
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = Y_train
    # getter function

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    # length function

    def __len__(self):
        return self.n_samples


# hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])
learning_rate = 0.001
num_epochs = 2000


dataset = ChatDataSet()
train_loader = DataLoader(
    dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)


device = torch.device('cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# loss and optimizer

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# training loop

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)

        # forward
        outputs = model(words)

        loss = criterion(outputs, labels)

        # backwards and optimizer step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.9f}')

print(f'final loss: {loss.item():.4f}')


data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete.file saved to {FILE}')
