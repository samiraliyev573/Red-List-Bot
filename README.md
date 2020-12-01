# Red-List-Bot
Red List bot that informs you about endangered species.



# Features: 

## Simple Graphical User Interface

A graphical user interface (GUI) was implemented into the A2-Extension allowing users to have a standard windows or apple GUI including buttons to resize the window, minimize the window or close the window, a file menu and clickable-buttons to send chat messages to our bot. 

For Graphical User Interface, I decided to go with tkinter library inside python since it is one of the popular ways to create GUI for the python app. The app consists of one main frame. First I created chatwindow which is basically the entire window. Then we created a scrollbar that is always on the right of chat window and follows it through the vertical axis. Then I created a text for displaying texts. I also made the scrollbar follow the text on y axis. Then we created a frame. This frame is later used to put user input field inside it. Inside user input field user would type their question/comment. I also added button that is used to send message. This button is on the right of the text input field and it is used to talk to the get_ouput function. Get output function basically gets user input from the text input field, pastes inside window and then sends to the chat method in chat.py and saves the result string inside chatbotanswer variable. Then it prints the answer from chatbot’s name, and also puts it inside the window. Once this is done, app clears the input field so user doesn’t have to delete by themselves every time. For tkinter to work, it runs the main loop which continuously runs all the time. Therefore, binding get_output method to the main loop will make the app continuously ask for user input and return answer, just like a while loop that we had from the assignment. There is also exit button under settings menu that lets user to exit the app. Additionally, there is clear chat button on file menu which clears the entire conversation history so you can start as if nothing was written before.

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/GUIScreenshot.png)

## UserInputSpellChecking

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/InputSpellChecking.png)

![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/InputSpellCheckingProof1.png)
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/Input%20SpellCheckingProof2.png)
![Screenshot](https://github.com/samiraliyev573/Red-List-Bot/blob/main/images/InputSpellCheckingProof3.png)


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
  




