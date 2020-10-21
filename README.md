# Red-List-Bot
Red List bot that informs you about endangered species



# How to run chatbot

1. Clone the repository from github

2. Have python installed (python 3.6+ )

3. Run pip install nltk

4. Run pip install torch torchvision if you are in mac or Run pip install torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

5. Open terminal and navigate to the src folder

6. Run chat.py (if data.pth does not get clones, run train.py before chat.py)

Enjoy the ChatBot ;)



# About the ChatBot

This chat bot uses nltk packages and uses Natural Language Processing. All of the code necessary to run it can be found in src folder. Source folder has 6 files.
  * nlty-utils.py file basically designed to tokenize, stem and put them in bag of words. Tokenizing will put the string into the words, punctiation and numbers.
  Example: "How are you will" be changed into "How", "are", "you". Stemming will seperate roots from the actual word. Example: universe and university will be    turned into univers. bag_of_words method will create array that is 0 if the sentence has specific word in it or make it 1 if it has that specific work. Purpose of this is to generate aray of 1s and 0s then use it for training our model.
  * model.py file is about creating Neural Network for out data. It will create three linear layers, which are input layer, hidden layer and the output layer. 
  * train.py class is for training the model. Note: If github clone you have downloaded already has data.pth file, you may straight away run chat.py file. It will load contents of intents.json into the intents var. From there, it will use list of which words to ignore and then use stemming and tokenization methods from nlty-utils class. After that, it will sord them all uniquely into the set and start the training model. Once the model is done, it will save it in data.pth so chat.py can use it for chatting with the user. 
  * chat.py file will read input from the user, tokenize it and then put it in bag of words. Then it will predict the answer. If the probability of the predicted answer is greater than 0.70, it will randomly pick responses from intents.json and present it to the user. If the probability is not high enough, it will simply assume that he has no answer for that question and print I do not understand. 
  * Intents.json is about tags, patterns and responses. Tags are overall intent and each have pattern and response. Pattern is basically question and response is basically an answer. From the question user asks, it RedListBot will predict appropriate tag and patterns and try to find the response from this file.
  




