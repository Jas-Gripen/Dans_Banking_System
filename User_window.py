from tkinter import Toplevel, Label, Button 
from bank_system import Bank_system
from Assets_window import Assets_window
from Deposit_window import Deposit_window
from Withdraw_window import Withdraw_window
from Transfer_window import Transfer_window
class User_window:
    def start_user_window(self, home_screen, account_id, username):
        self.account_id = account_id
        self.username = username
        self.home_window = home_screen
        print('userwindow:',self.account_id)

        self.user_window = Toplevel(home_screen)
        self.user_window.geometry('250x300')
        self.user_window.title('Your account [{}]'.format(username))

        #Labels
        self.details_label = Label(self.user_window, text = 'How may I help you?', font=('Calibri',20))
        self.details_label.grid(row=0, column=0, sticky='N')

        #Assets label
        self.assets_label = Label(self.user_window, font=('Calibri',12))
        self.assets_label.grid(row=4, sticky='N')

        #Buttons
        self.deposit_button = Button(self.user_window, text='Deposit', font=('Calibri', 16), width=10,command=lambda: self.deposit())
        self.deposit_button.grid(row=1, column=0, sticky='N')
        
        self.withdraw_button = Button(self.user_window, text='Withdraw', font=('Calibri', 16), width=10,command=lambda: self.withdraw())
        self.withdraw_button.grid(row=2, column=0, sticky='N')
        
        self.transfer_button = Button(self.user_window, text='Transfer', font=('Calibri', 16), width=10,command=lambda: self.transfer())
        self.transfer_button.grid(row=3, column=0, sticky='N')

        self.view_assets_button = Button(self.user_window, text='View assets', font=('Calibri', 16), width=10,command=lambda: self.view_assets(home_screen))
        self.view_assets_button.grid(row=4, column=0, sticky='N', padx=5)

        self.logout_button = Button(self.user_window, text='Logout', font=('Calibri', 16), width=10,command=lambda: self.user_window.destroy())
        self.logout_button.grid(row=5, column=0, sticky='N', padx=5)

    def deposit(self):
        Deposit_window().start_deposit_window(self.home_window, self.account_id, self.username)
    
    def withdraw(self):
        Withdraw_window().start_withdraw_window(self.home_window, self.account_id, self.username)
    
    def transfer(self):
        Transfer_window().start_transfer_window(self.home_window, self.account_id, self.username)
    
    def view_assets(self, home_screen):
        Assets_window().start_assets_window(home_screen, self.account_id, self.username)

    def remove_stuff(self):
        self.deposit_button.destroy()
        self.withdraw_button.destroy()
        self.transfer_button.destroy()
        self.view_assets_button.destroy()
        self.logout_button.destroy()
        self.details_label.destroy()
        self.assets_label.destroy()