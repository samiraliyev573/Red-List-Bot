import random
import json
import torch
from model import NeuralNet
from nltkproperties import bag_of_words, tokenize, synonym_recognition, show_part_of_speech

device = 'cuda' if torch.cuda.is_available() else 'cpu'

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]

tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)

model.load_state_dict(model_state)

model.eval()

bot_name = "Red List Bot"

# Made the commented code into a function so gui.py can ask and this function can return
def chat(sentence):
    pos_sentence = show_part_of_speech(sentence)
    print(pos_sentence)
    if sentence == 'quit':
        return "Quit has been asked"
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    
    
    
    X = torch.from_numpy(X).to(device)
    
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    
    # check if the probability of this tag is high enough
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.70:

        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "I do not understand"
        



#print("Let's chat! type 'quit' to exit")
#while True:
#    sentence = input('You: ')
#    if sentence == 'quit':
#        break
#
#    sentence = tokenize(sentence)
#    X = bag_of_words(sentence, all_words)
#    X = X.reshape(1, X.shape[0])
#    X = torch.from_numpy(X).to(device)
#
#    output = model(X)
#    _, predicted = torch.max(output, dim=1)
#    tag = tags[predicted.item()]
#    # check if the probability of this tag is high enough
#    probs = torch.softmax(output, dim=1)
#    prob = probs[0][predicted.item()]

#    if prob.item() > 0.75:

#        for intent in intents["intents"]:
#            if tag == intent["tag"]:
#                print(f"{bot_name}: {random.choice(intent['responses'])}")
#    else:
#        print(f"{bot_name}: I do not understand...")
