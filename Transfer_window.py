from tkinter import Toplevel, StringVar, Label, Button, Entry 
from bank_system import Bank_system
from Assets_window import Assets_window

class Transfer_window:
    def start_transfer_window(self, home_screen, account_id, username):
        self.account_id = account_id
        self.transfer_window = Toplevel(home_screen)
        self.transfer_window.geometry('500x180')
        self.transfer_window.title('Transfer [{}]'.format(username))

        self.temp_username = StringVar()
        self.temp_amount = StringVar()
        
        #Labels
        detail_label = Label(self.transfer_window, text = 'Please enter a username and the amount', font=('Calibri',20))
        detail_label.grid(row=0, column=0, sticky='N')

        username_lable = Label(self.transfer_window, text = 'username', font=('Calibri',16))
        username_lable.grid(row=1, column=0, sticky='W')

        amount_lable = Label(self.transfer_window, text = 'Amount', font=('Calibri',16))
        amount_lable.grid(row=2, column=0, sticky='W')

        #hidden label
        self.hidden_label = Label(self.transfer_window, font=('Calibri',12))
        self.hidden_label.grid(row=5, sticky='N')

        #Error label
        self.error_label = Label(self.transfer_window, font=('Calibri',12))
        self.error_label.grid(row=4, sticky='N')

        #Entries
        self.username_entry = Entry(self.transfer_window, textvariable=self.temp_username)
        self.username_entry.grid(row=1, column=0)

        self.amount_entry = Entry(self.transfer_window, textvariable=self.temp_amount)
        self.amount_entry.grid(row=2, column=0)

        #Buttons
        ok_button = Button(self.transfer_window, text='Ok', font=('Calibri', 16), width=10,command=lambda: self.start_transfer())
        ok_button.grid(row=3, column=0, sticky='E')

        go_back_button = Button(self.transfer_window, text='Go back', font=('Calibri', 16), width=10,command=lambda: self.transfer_window.destroy())
        go_back_button.grid(row=3, column=0, sticky='W', padx=5)
        #Note to self, add function to close all windows on logout

    def start_transfer(self):
        username = self.temp_username.get()
        amount = self.temp_amount.get()
        if(self.check_user_input(username, amount)):
            self.finish_transfer(username, amount)

    
    def finish_transfer(self, username, amount):
        target_id = Bank_system().get_target_account_id(username)
        Bank_system().transfer_assets(self.account_id, target_id, amount)
        self.username_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')
        self.transfer_window.geometry('500x200')
        self.error_label.config(fg='green',text='The transfer was successfully made')
        #Note to self, add function to check if the deposit was succesful
    
    def check_user_input(self, username, amount):
        lower_bound = '200'
        horozontal_bound = '500'
        if((" " in username) or (" " in amount)):
            print('Spaces are not allowed')
            self.transfer_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Spaces are not allowed')
            return False
        elif(username == '' and amount == ''):
            self.transfer_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Please enter a username and the amount')
            return False
        elif(username == ''):
            self.transfer_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Please enter a username')
            return False
        elif(username == '' and amount == ''):
            self.transfer_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='Please enter the amount')
            return False
        elif(not(amount.isdecimal())):
            self.transfer_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='The ammount has to be given in numbers')
            return False
        elif (Bank_system().check_target_user(username)):
            return True
        else:
            self.transfer_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.error_label.config(fg='red',text='The user does not exist')
            return False
    