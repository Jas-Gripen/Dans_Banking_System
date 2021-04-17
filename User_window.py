# Class: User_window
# Description: Pop-up window for the user home window
# Author: Daniel Gripenstedt  
from tkinter import Toplevel, Label, Button, Entry, StringVar
from bank_system import Bank_system
from Assets_window import Assets_window
from Deposit_window import Deposit_window
from Withdraw_window import Withdraw_window
from Transfer_window import Transfer_window
class User_window:
    # Build the user window with all of the labels and buttons
    def start_user_window(self, home_screen, account_id, username, password):
        self.account_id = account_id
        self.first_username = username
        self.first_password = password
        self.home_window = home_screen
        print('userwindow:',self.account_id)

        self.user_window = Toplevel(home_screen)
        self.user_window.geometry('200x250')
        self.user_window.title('Your account [{}]'.format(username))

        #Labels
        self.details_label = Label(self.user_window, text = 'How may I help you?', font=('Calibri',16))
        self.details_label.grid(row=0, column=0, sticky='N')

        #Assets label
        self.assets_label = Label(self.user_window, font=('Calibri',12))
        self.assets_label.grid(row=4, sticky='N')

        #Buttons
        self.deposit_button = Button(self.user_window, text='Deposit', font=('Calibri', 12), width=12,command=lambda: self.deposit())
        self.deposit_button.grid(row=1, column=0, sticky='N')
        
        self.withdraw_button = Button(self.user_window, text='Withdraw', font=('Calibri', 12), width=12,command=lambda: self.withdraw())
        self.withdraw_button.grid(row=2, column=0, sticky='N')
        
        self.transfer_button = Button(self.user_window, text='Transfer', font=('Calibri', 12), width=12,command=lambda: self.transfer())
        self.transfer_button.grid(row=3, column=0, sticky='N')

        self.view_assets_button = Button(self.user_window, text='View assets', font=('Calibri', 12), width=12,command=lambda: self.view_assets(home_screen))
        self.view_assets_button.grid(row=4, column=0, sticky='N', padx=5)

        self.delete_account_button = Button(self.user_window, text='Delete account', font=('Calibri', 12), width=12,command=lambda: self.start_delete_account())
        self.delete_account_button.grid(row=5, column=0, sticky='N', padx=5)

        self.logout_button = Button(self.user_window, text='Logout', font=('Calibri', 12), width=12,command=lambda: self.user_window.destroy())
        self.logout_button.grid(row=6, column=0, sticky='N', padx=5)

    # Start deposit window
    def deposit(self):
        Deposit_window().start_deposit_window(self.home_window, self.account_id, self.first_username)
    
    # Start withdraw window
    def withdraw(self):
        Withdraw_window().start_withdraw_window(self.home_window, self.account_id, self.first_username)
    
    # Start transfer window
    def transfer(self):
        Transfer_window().start_transfer_window(self.home_window, self.account_id, self.first_username)
    
    # Start assets window
    def view_assets(self, home_screen):
        Assets_window().start_assets_window(home_screen, self.account_id, self.first_username)
    
    # Start to rebuild the user window as a "delete account window"
    def start_delete_account(self):
        self.remove_stuff()
        self.setup_delete_stuff()
        self.finish_delete_account()
    
    # Build the delete account window
    def setup_delete_stuff(self):
        self.user_window.geometry('450x160')
        #Temp varibles
        self.temp_username = StringVar()
        self.temp_password = StringVar()

        #Labels
        self.details_label = Label(self.user_window, text = 'Please enter your username and password', font=('Calibri',18))
        self.details_label.grid(row=0, column=0, sticky='N')

        self.username_lable = Label(self.user_window, text = 'Username', font=('Calibri',16))
        self.username_lable.grid(row=1, column=0, sticky='W')

        self.password_lable = Label(self.user_window, text = 'Password', font=('Calibri',16))
        self.password_lable.grid(row=2, column=0, sticky='W')

        #Error label
        self.error_label = Label(self.user_window, font=('Calibri',12))
        self.error_label.grid(row=4, sticky='N')

        #Entries
        self.username_entry = Entry(self.user_window, textvariable=self.temp_username)
        self.username_entry.grid(row=1, column=0)

        self.password_entry = Entry(self.user_window, textvariable=self.temp_password, show='*')
        self.password_entry.grid(row=2, column=0)

        #Buttons
        self.ok_button = Button(self.user_window, text='Delete account', font=('Calibri', 12), width=12,command=lambda: self.finish_delete_account())
        self.ok_button.grid(row=3, column=0, sticky='E')

        self.cancel_button = Button(self.user_window, text='Cancel', font=('Calibri', 12), width=12,command=lambda: self.cancel())
        self.cancel_button.grid(row=3, column=0, sticky='W', padx=5)
    
    # Check if user input is valid and delete the account
    def finish_delete_account(self):
        username = self.temp_username.get()
        password = self.temp_password.get()
        if(self.check_user_input(username, password)):
            Bank_system().delete_account(self.account_id)
            self.user_window.destroy()

    # Cancel the deletion of the account and rebuild the the user home window
    def cancel(self):
        self.user_window.destroy()
        self.start_user_window(self.home_window, self.account_id, self.first_username, self.first_password)

    # Remove all of the stuff in the user window
    def remove_stuff(self):
        self.deposit_button.destroy()
        self.withdraw_button.destroy()
        self.transfer_button.destroy()
        self.view_assets_button.destroy()
        self.logout_button.destroy()
        self.details_label.destroy()
        self.assets_label.destroy()
        self.delete_account_button.destroy()
    
    # Check if user input is valied and give warning if it is not
    def check_user_input(self, username, password):
        lower_bound = '180'
        horozontal_bound = '480'
        if((" " in username) or (" " in password)):
            print('Spaces are not allowed')
            self.user_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Spaces are not allowed')
            return False
        elif(username == '' and password == ''):
            self.user_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Please enter your username and password')
            return False
        elif(username == ''):
            self.user_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Please enter your username')
            return False
        elif(password == ''):
            self.user_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Please enter your password')
            return False
        elif (username == self.first_username and password == self.first_password):
            return True
        else:
            self.user_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Wrong username or password')
            return False