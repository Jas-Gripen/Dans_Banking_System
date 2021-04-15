from tkinter import Toplevel, StringVar, Label, Button, Entry 
from bank_system import Bank_system

class Register_window:   
    def register(self, home_screen):
        print('register function')

        #Temp varibles
        self.temp_username = StringVar()
        self.temp_password = StringVar()

        self.register_screen = Toplevel(home_screen)
        self.register_screen.geometry('450x160')
        self.register_screen.title('Register')

        #Labels
        self.details_label = Label(self.register_screen, text = 'Please enter yor details below', font=('Calibri',26))
        self.details_label.grid(row=0, column=0, sticky='N')

        self.username_lable = Label(self.register_screen, text = 'Username', font=('Calibri',16))
        self.username_lable.grid(row=1, column=0, sticky='W')

        self.password_lable = Label(self.register_screen, text = 'Password', font=('Calibri',16))
        self.password_lable.grid(row=2, column=0, sticky='W')

        #Error label
        self.error_label = Label(self.register_screen, font=('Calibri',12))
        self.error_label.grid(row=4, sticky='N')

        #Entries
        self.username_entry = Entry(self.register_screen, textvariable=self.temp_username)
        self.username_entry.grid(row=1, column=0)

        self.password_entry = Entry(self.register_screen, textvariable=self.temp_password, show='*')
        self.password_entry.grid(row=2, column=0)

        #Buttons
        self.ok_button = Button(self.register_screen, text='Ok', font=('Calibri', 16), width=10,command=lambda: self.register_user())
        self.ok_button.grid(row=3, column=0, sticky='E')

        #self.cancel_button = Button(self.register_screen, text='Cancel', font=('Calibri', 16), width=10,command=self.register_screen.destroy)
        self.cancel_button = Button(self.register_screen, text='Cancel', font=('Calibri', 16), width=10,command=lambda: self.register_screen.destroy())
        self.cancel_button.grid(row=3, column=0, sticky='W', padx=5)
    
    def close(self):
        print("close")
        #button.place_forget()
        self.register_screen.destroy()

    def remove_button(self, button):
        print("remove_button")
        #button.place_forget()
    
    def register_user(self):
        import time
        username = self.temp_username.get()
        password = self.temp_password.get()
        lower_bound = '180'
        self.register_screen.geometry('450x{}'.format(lower_bound))
        if((" " in username) or (" " in password)):
            self.error_label.config(fg='red',text='Spaces are not allowed')
        elif(username == '' and password == ''):
            self.error_label.config(fg='red',text='Please enter a username and a password')
        elif(username == ''):
            self.error_label.config(fg='red',text='Please enter a username')
        elif(password == ''):
            self.error_label.config(fg='red',text='Please enter a password')
        elif(Bank_system().check_username(username)):
            self.error_label.config(fg='red',text='Username is already taken')
        elif(not(Bank_system().check_username(username))):
            Bank_system().add_user_to_db(username, password)
            self.remove_register_GUI()
            self.register_screen.update()
            time.sleep(1)
            self.close()
    
    def remove_register_GUI(self):
        self.details_label.config(fg='green',text='Register complete')
        self.ok_button.destroy()
        self.cancel_button.destroy()
        self.username_lable.destroy()
        self.password_lable.destroy()
        self.username_entry.destroy()
        self.password_entry.destroy()
        self.error_label.destroy()