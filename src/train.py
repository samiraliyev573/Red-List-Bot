# imports
import json
import torch
import torch.nn as nn
from nltkproperties import tokenize, stem, bag_of_words, show_part_of_speech, synonym_recognition
import numpy as np
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet
import shutil
# opening intents.json because it contains tags patterns and responses
with open('intents.json', 'r+') as i:
    # load contents of json file into intents
    intents = json.load(i)

    print(intents)

src="intents.json"
dst="intentsfortrain.json"
shutil.copy(src,dst)

with open('intentsfortrain.json', 'r+') as i:
    # load contents of json file into intents
    intentsfortrain = json.load(i)


#"patterns": [
#        "Hi",
#        "Hey",
#        "How are you?",
#        "Is anyone there?",
#        "Hello",
#        "Greetings and Salutations",
#        "Good day"
#      ],  


for  (patternindex,intent) in enumerate( intentsfortrain['intents'], start = 1):
    for pattern in intent['patterns']:
        print("Sentence" ,pattern)
        print("Index",patternindex)
        patter_list_sentence = show_part_of_speech(pattern)
        for i in patter_list_sentence:
            print("Word: " ,i[0])
            print("Tag:",i[1])
            newsentence = ""
            newpattern = {"patterns": "pattern"}
            if i[1] == 'JJ': 
                synonyms = synonym_recognition(i[0])
                print("Synonyms for the word is: ",synonyms)
                for synonym in synonyms:
                    newsentence = pattern.replace(i[0], synonym)+" \n"
                
                print(newsentence)
                #    intentsfortrain["0"]["patterns"].append({newsentence})
                #newpattern["patterns"] = newsentence
                #print(newpattern)
            


    





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
num_epochs = 10000


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
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

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
