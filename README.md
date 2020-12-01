# Red-List-Bot
Red List bot that informs you about endangered species.



# Features: 

## Simple Graphical User Interface: 

A graphical user interface (GUI) was implemented into the A2-Extension allowing users to have a standard windows or apple GUI including buttons to resize the window, minimize the window or close the window, a file menu and clickable-buttons to send chat messages to our bot. 

For Graphical User Interface, I decided to go with tkinter library inside python since it is one of the popular ways to create GUI for the python app. The app consists of one main frame. First I created chatwindow which is basically the entire window. Then we created a scrollbar that is always on the right of chat window and follows it through the vertical axis. Then I created a text for displaying texts. I also made the scrollbar follow the text on y axis. Then we created a frame. This frame is later used to put user input field inside it. Inside user input field user would type their question/comment. I also added button that is used to send message. This button is on the right of the text input field and it is used to talk to the get_ouput function. Get output function basically gets user input from the text input field, pastes inside window and then sends to the chat method in chat.py and saves the result string inside chatbotanswer variable. Then it prints the answer from chatbot’s name, and also puts it inside the window. Once this is done, app clears the input field so user doesn’t have to delete by themselves every time. For tkinter to work, it runs the main loop which continuously runs all the time. Therefore, binding get_output method to the main loop will make the app continuously ask for user input and return answer, just like a while loop that we had from the assignment. There is also exit button under settings menu that lets user to exit the app. Additionally, there is clear chat button on file menu which clears the entire conversation history so you can start as if nothing was written before.

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/GUIScreenshot.png)

## User Input SpellChecking:

Our Red List Bot uses natural language processing tools such as stemming and tokenization. This means that present, past, future tense doesnt matter and bot takes the root of every word. When user asks a question, bot splits the sentence into words and punctiations, stems the word(extracting root of the word) and then asks from its database. Model is also trained using stemming and tokenization to make it more fluent. 

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/InputSpellChecking.png)

As you can see from the screenshot, user asks `How aer you` or `See ya later` or `Which are animals endanger` but bot still recognizes this as greeting response. This is because we have set variance high enough to make it flexible while making sure that it doesnt answer randomly to every question and let user know when it doesnt have the answer.
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/InputSpellCheckingProof1.png)
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/Input%20SpellCheckingProof2.png)
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/InputSpellCheckingProof3.png)

## Part of Speech Tagging:
POS Tagging(Part of speech tagging) is a very important feature in the development of the bot. It is used to identify nouns, adjectives, verbs and every phrase. We created `show_part_of_speech `function in `nltkproperties.py` which is the primary function for it. Sample output shows that method working on the user input. This very important because later we will be using it to identify adjectives in a sentence and implement for synonym recognition

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/POSTagging.png)
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/POSTaggingproof.png)

 We can analyze one of the lines in the terminal output. 
`[('Tell', 'VB'), ('me', 'PRP'), ('more', 'JJR'), ('about', 'IN'), ('Leopards', 'NNS')]`
It identifies word Tell as VB(verb, base form), me as PRP(personal pronoun), more as JJR(adjective comparative), about as IN(preposition/subordinating conjunction) and Leopards as NNS(noun plural)

## Synonym Recognition:

Synonym recognition is used for recognizing synonyms in the sentence. In our case, we had a function called synonym_recognition that returns the list of synonyms associated with the word. 
This function now is being used in train.py class. In train.py I created an algorithm that goes through every pattern in intents.json, identifies adjectives using pos tagging, creates new sentence by replacing previous word with the synonym of the word. Then it creates list of sentences including every new sentence with the new synonym. It then appends the newsentence list to the previous pattern. If our pattern were to be `How big are rhinos?`, new pettern would be `How big are rhinos, How large are rhinos, How grown are Rhinos, How sizeable are Rhinos, How mammoth are Rhinos` and more.



![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/SynonymRecognition.png)

You can see from these screenshots that we do not have word near extinct and grown in the intents file. Bot was smart enough to recognize that the near is synonym to close and grown is synonym to big. 

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/SynonymRecognitionProof.png)
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/SynonymRecognitionProof2.png)

That being said, there are still a lot of limitations with the synonym recognition algorithm. It was very complex to implement so we only tried it on adjectives to prove that this is fully functional. Implementing them on verbs, nouns and pronounts will take more complexity yet can be completed with minor changes to methods and classes. 




## Text to Speech:

One of the great features of the app is text to speech functionality. It is mainly for the disability support. When chatbot returns an answer, it also talks by using gtts(google text-to-speech) library to convert text into speech and save it in the audio file. Then it plays the audio file by using playsound library on windows, pygame library on macos. Once it finishes speaking the audio file, it automatically deletes using os package in python. For this to work, we had to use threading since main loop runs continiously and we need to provide exclusion to speech. 
Everytime, before chatbot starts to speak, it creates a new thread and plays it with the help of threading package in python

## Categorized String Matching:

Our intents.json file is basically a response tree. User asks a question, and model decides the category of the question which is represented as `tag` and then ideantifies which question it is by the probability of the user input being related to the question(pattern) in tag. If the probability is higher than 0.75(75%), model picks random response from the respose list and returns it to the user. 
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/categorizedstringmatching.png)

# How to run chatbot 
## Note: If you are using windows, simply double click on the InstallationWindows.bat and it will install all the necessary files.


1. Clone the repository from github
https://github.com/samiraliyev573/Red-List-Bot

2. Have python installed (python 3.6+ )
https://www.python.org/downloads/

3. Have anaconda installed. (In windows when downloading anaconda, check the box that says add anaconda to path environment variables.)
Install anaconda here: https://docs.conda.io/projects/conda/en/latest/user-guide/install/

4. Now we create anaconda environment so whatever we do will be outside our system and wont do any harm to our currently installed packages. Type `conda create -n projenv python=3.8` (if this command doesnt work, update your conda by typing `conda update conda`)

5. Now open terminal and navigate to the src folder of the project(You can also do it by opening in visual studio code and selecting new terminal.)

6. Inside the src folder, type `conda activate projenv`. Now our virtual environment is active inside this folder. Only thing left is to install necessary packages. 
  Run: `conda install pytorch torchvision torchaudio cpuonly -c pytorch` if in windows or 
  `conda install pytorch torchvision torchaudio -c pytorch` if in macos.
  
  Run `conda install nltk`
  Run `pip3 install gtts`
  Run `pip3 install pygame`
  Run `pip3 install playsound`
  Run `pip3 install numpy`
  
7. Last step is to type `python3 gui.py` which will run the python file.


Enjoy the ChatBot ;)



# About the ChatBot

This chat bot uses nltk packages and uses Natural Language Processing. All of the code necessary to run it can be found in src folder. Source folder has 6 files.
  * nltkproperties.py file basically designed to tokenize, stem and put them in bag of words. Tokenizing will put the string into the words, punctiation and numbers.
  Example: "How are you will" be changed into "How", "are", "you". Stemming will seperate roots from the actual word. Example: universe and university will be    turned into univers. bag_of_words method will create array that is 0 if the sentence has specific word in it or make it 1 if it has that specific work. Purpose of this is to generate aray of 1s and 0s then use it for training our model.
  * model.py file is about creating Neural Network for out data. It will create three linear layers, which are hidden layer, input layer  and the output layer. 
  * train.py class is for training the model. Note: If github clone you have downloaded already has data.pth file, you may straight away run chat.py file. It will load contents of intents.json into the intents var. From there, it will use list of which words to ignore and then use stemming and tokenization methods from nlty-utils class. After that, it will sort them all uniquely into the set and start the training model. Once the model is done, it will save it in data.pth so chat.py can use it for chatting with the user. 
  * chat.py file will read input from the user, tokenize it and then put it in bag of words. Then it will predict the answer. If the probability of the predicted answer is greater than 0.75, it will randomly pick responses from intents.json and present it to the user. If the probability is not high enough, it will simply assume that he has no answer for that question and print I do not understand. 
  * Intents.json is about tags, patterns and responses. Tags are overall intent and each have pattern and response. Pattern is basically question and response is basically an answer. From the question user asks, it RedListBot will predict appropriate tag and patterns and try to find the response from this file.
  




