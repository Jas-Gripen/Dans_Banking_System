from tkinter import Toplevel, StringVar, Label, Button, Entry 
from bank_system import Bank_system
from User_window import User_window
class Login_window:
    def login_start(self, home_screen):
        self.tmp_home_screen = home_screen
        self.login_window = Toplevel(home_screen)
        self.login_window.geometry('450x160')
        self.login_window.title('Login')
        self.login()

    def login(self):
        #Temp varibles
        self.temp_username = StringVar()
        self.temp_password = StringVar()

        #Labels
        self.details_label = Label(self.login_window, text = 'Please enter username and password', font=('Calibri',20))
        self.details_label.grid(row=0, column=0, sticky='N')

        self.username_lable = Label(self.login_window, text = 'Username', font=('Calibri',16))
        self.username_lable.grid(row=1, column=0, sticky='W')

        self.password_lable = Label(self.login_window, text = 'Password', font=('Calibri',16))
        self.password_lable.grid(row=2, column=0, sticky='W')

        #Error label
        self.error_label = Label(self.login_window, font=('Calibri',12))
        self.error_label.grid(row=4, sticky='N')

        #Entries
        self.username_entry = Entry(self.login_window, textvariable=self.temp_username)
        self.username_entry.grid(row=1, column=0)

        self.password_entry = Entry(self.login_window, textvariable=self.temp_password, show='*')
        self.password_entry.grid(row=2, column=0)

        #Buttons
        self.ok_button = Button(self.login_window, text='Ok', font=('Calibri', 16), width=10,command=lambda: self.login_db())
        self.ok_button.grid(row=3, column=0, sticky='E')

        self.cancel_button = Button(self.login_window, text='Cancel', font=('Calibri', 16), width=10,command=lambda: self.login_window.destroy())
        self.cancel_button.grid(row=3, column=0, sticky='W', padx=5)
    
    def login_db(self):
        username = self.temp_username.get()
        password = self.temp_password.get()
        print(username)
        print(password)

        lower_bound = '180'
        if((" " in username) or (" " in password)):
            print('Spaces are not allowed')
            self.login_window.geometry('450x{}'.format(str(lower_bound)))
            self.error_label.config(fg='red',text='Spaces are not allowed')
        elif(username == '' and password == ''):
            print('1')
            self.login_window.geometry('450x{}'.format(str(lower_bound)))
            self.error_label.config(fg='red',text='Please enter a username and a password')
        elif(username == ''):
            print('2')
            self.login_window.geometry('450x{}'.format(str(lower_bound)))
            self.error_label.config(fg='red',text='Please enter a username')
        elif(password == ''):
            print('3')
            self.login_window.geometry('450x{}'.format(str(lower_bound)))
            self.error_label.config(fg='red',text='Please enter a password')
        elif(Bank_system().check_user(username, password)):        
            print('4')        
            self.remove_login_GUI()
            self.close()
            account_id = Bank_system().get_account_id(username, password)
            print(account_id)
            User_window().start_user_window(self.tmp_home_screen, account_id, username)
    
    def close(self):
        self.login_window.destroy()
    
    def remove_login_GUI(self):
        self.details_label.config(fg='green',text='Register complete')
        self.ok_button.destroy()
        self.cancel_button.destroy()
        self.username_lable.destroy()
        self.password_lable.destroy()
        self.username_entry.destroy()
        self.password_entry.destroy()