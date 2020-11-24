# tkinter package for making gui and graphical interface
from tkinter import *

# messagebox method inside tkinter
import tkinter.messagebox



# importing chat method that has new chat function that returns trained data's answer
from chat import chat


# importing threading to create another thread for the text-to speech functionality
import threading

# gtts is google text to speech library for concerting text to speech
from gtts import gTTS

# pygame has class called mixer that plays audio
# for mac os
from pygame import mixer

# importing os for os related commands
import os

# importing library to play sound
# for windows
import playsound

# importing to differentiate between mac and windows
from sys import platform



# main interface for the gui
class ChatInterface(Frame):
    # initializing frame
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        #Menu: 
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
        
        top_menu = Menu(menu, tearoff=0)
        # top menu which is settings has 3 properties
        menu.add_cascade(label="Settings", menu=top_menu)

        # first property is about us shows that the project is made by students in this course
        top_menu.add_command(label="About us", command=self.project_about)
        
        # second property is clear chat which clears the chat
        top_menu.add_command(label="Clear Chat", command=self.chat_clean)

        # third property is exit app. Dont know exactly why but seemed like a feature to implement since a lot of apps have this button.
        top_menu.add_command(label="Exit",command=self.exit_app)
        



        # Creating chat wondow
        self.chat_window = Frame(self.master, bd=6)
        # making it expand and fill both sides of the gui
        self.chat_window.pack(expand=True, fill=BOTH)


        # Creating scroll bar inside chat window
        self.scrollbar = Scrollbar(self.chat_window)


        # Making scroll bar fill the chatwindow in Y axis and position it in the right side of the window
        self.scrollbar.pack(fill=Y, side=RIGHT)



        # Text that is shown in the window
        self.text_list = Text(self.chat_window, yscrollcommand=self.scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Arial", 
                             width=10, height=1)

        # make it expand and fill both sides if necessary
        self.text_list.pack(expand=True, fill=BOTH)

        # adding this makes scrolling active and follows text in vertical direction
        self.scrollbar.config(command=self.text_list.yview)

        # Frame for user input
        self.frame_input = Frame(self.master, bd=1)
        # Put it on the left side of the screen and fill both sides
        self.frame_input.pack(side=LEFT, fill=BOTH, expand=True)

        # field that user actuall types. Put it inside Frame that we created for user input
        self.input_field = Entry(self.frame_input, bd=1, justify=LEFT)
        # give it some parameters
        self.input_field.pack(fill=X, padx=6, pady=6, ipady=3)


        # frame for button
        self.button_frame = Frame(self.master, bd=0)
        self.button_frame.pack(fill=BOTH)

        # Button to send it to bot. Put it inside the button frame and call get_output function when button pressed.
        self.send_button = Button(self.button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.get_output(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=7)

        # bind the main function to get_output
        self.master.bind("<Return>", self.get_output)

    # method for clearing chat
    def chat_clean(self):

        # clear all the text inside text widget
        self.text_list.config(state=NORMAL)
        self.text_list.delete(1.0, END)
        self.text_list.delete(1.0, END)
        self.text_list.config(state=DISABLED)
    
    # for quittng the chat
    def exit_app(self):
        exit() 
    
    # for displaying about us info for the user inside the message box
    def project_about(self):
        tkinter.messagebox.showinfo(title="COSC 310 Project Group 1:", message= "Samir Aliyev - Lead Developer\nWesley Burchnall - Project Manager\nMichael Bartinski - Documentation\n Maruf Zubery- Documentation \n Daniel Inglot - Presentation\n")



    # function for playing sound
    def playSound(self,answer):
        audio_name = 'audio.mp3'
        
        # initialize google text to speech
        tts = gTTS(answer)
        
        # save the audio file of the response inside audio.mp3 
        tts.save(audio_name)

        if platform == "darwin":
             # initialize mixer
            mixer.init()

            # load the saved audio
            mixer.music.load(audio_name)

            # play the saved audio
            mixer.music.play()
        else:
            # play the audio file that google text to speech saved
            playsound.playsound(audio_name)

        # remove the audio file after playing it
        os.remove(audio_name)

 
    # function for sending user message to chatbot and receiving the answer.
    def get_output(self, message):

        # get user input from input field
        user_input = self.input_field.get()

        # string combining user input and making it from user perspective
        usertext = "You : " + user_input + "\n"

        # insert the string 
        self.text_list.configure(state=NORMAL)
        self.text_list.insert(END, usertext)
        self.text_list.configure(state=DISABLED)

        # Make user to see end text. This means scrollbar will automatically scroll down
        self.text_list.see(END)

        # get chatbotanswer fron chat function insde chat.py
        chatbotanswer=chat(user_input)

        # string combining chatbot output and making it from Red-List bot's perspective
        answer="Red-List Bot : " + chatbotanswer + "\n"

        # insert the string 
        self.text_list.configure(state=NORMAL)

        self.text_list.insert(END, answer)
        self.text_list.configure(state=DISABLED)

        # Make user to see end text. This means scrollbar will automatically scroll down
        self.text_list.see(END)

        # clear the input field automatically so user doesnt delete everytime
        self.input_field.delete(0,END)

       
        # create thread for voice and call playSound function
        voiceThread = threading.Thread(target=self.playSound, args=(chatbotanswer,))
        # start the voicethread
        voiceThread.start() 

# initializing gui as TK         
gui=Tk()

# gui is now a part of Chat Interface
ChatInterface(gui)

# give it a size
gui.geometry("400x600")

# title for GUI
gui.title("RedList-Bot")

# Mouse animal icon by Icons8

photo = PhotoImage(file = "redlist_logo.png")
gui.iconphoto(False, photo)


# starting the  main loop
gui.mainloop()

