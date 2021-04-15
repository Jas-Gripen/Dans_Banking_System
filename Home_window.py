from tkinter import Tk, Label, Button 
from Register_window import Register_window
from Login_window import Login_window
from Exit_window import Exit_window
class Home_window:
    def __init__(self):
        self.home_window = Tk()
        self.home_window.geometry('500x350')
        self.home_window.title('Dan\'s Banking System')
        title_lable = Label(self.home_window, text = 'Dan\'s Banking System', font=('Calibri',38))
        title_lable.grid(row=0, column=0, sticky='N')
        self.start_home_window()

    def start_home_window(self):
        width = 15
        #Buttons
        login_button = Button(self.home_window, width=width, text='Login', font=('Calibri', 26), command=lambda: self.login())
        login_button.grid(row=1, column=0, sticky='N')

        register_button = Button(self.home_window, width=width, text='Register', font=('Calibri', 26), command=lambda: self.register())
        register_button.grid(row=2, column=0, sticky='N', pady=5)

        quit_button = Button(self.home_window, width=width, text='Exit program', font=('Calibri', 26), command=lambda: self.exit_program())
        quit_button.grid(row=3, column=0, sticky='N', pady=5)
    
    def login(self):
        Login_window().login_start(self.home_window)

    def register(self):
        Register_window().register(self.home_window)
    
    def exit_program(self):
        Exit_window().exit_program(self.home_window)

