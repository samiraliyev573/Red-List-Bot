# tkinter package for making gui and graphical interface
from tkinter import *

# importing chat method that has new chat function that returns trained data's answer
from chat import chat




# main interface for the gui
class ChatInterface(Frame):
    # initializing frame
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        #Menu: Planning to add more features through this
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)

        # Creating chat wondow
        self.chat_window = Frame(self.master, bd=6)
        # making it expand and fill both sides of the gui
        self.chat_window.pack(expand=True, fill=BOTH)


        # Creating scroll bar inside chat window
        self.scrollbar = Scrollbar(self.chat_window)


        # Making scroll bar fill the chatwindow in Y axis and position it in the right side of the window
        self.scrollbar.pack(fill=Y, side=RIGHT)


        
        # Text that is shown in the window
        self.text = Text(self.chat_window, yscrollcommand=self.scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Arial", 
                             width=10, height=1)

        # make it expand and fill both sides if necessary
        self.text.pack(expand=True, fill=BOTH)

        # adding this makes scrolling active and follows text in vertical direction
        self.scrollbar.config(command=self.text.yview)

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


    # function for sending user message to chatbot and receiving the answer.
    def get_output(self, message):

        # get user input from input field
        user_input = self.input_field.get()

        # string combining user input and making it from user perspective
        usertext = "You : " + user_input + "\n"

        # insert the string 
        #self.text.configure(state=NORMAL)
        self.text.insert(END, usertext)
        #self.text.configure(state=DISABLED)
        # Make user to see end text. This means scrollbar will automatically scroll down
        self.text.see(END)
        
        # get chatbotanswer fron chat function insde chat.py
        chatbotanswer=chat(user_input)

        # string combining chatbot output and making it from Red-List bot's perspective
        answer="Red-List Bot : " + chatbotanswer + "\n"

        # insert the string 
        #self.text.configure(state=NORMAL)

        self.text.insert(END, answer)
        #self.text.configure(state=DISABLED)

        # Make user to see end text. This means scrollbar will automatically scroll down
        self.text.see(END)

        # clear the input field automatically so user doesnt delete everytime
        self.input_field.delete(0,END)

# initializing gui as TK         
gui=Tk()

# gui is now a part of Chat Interface
ChatInterface(gui)

# give it a size
gui.geometry("400x600")

# title for GUI
gui.title("RedList-Bot")


# starting the  main loop
gui.mainloop()
