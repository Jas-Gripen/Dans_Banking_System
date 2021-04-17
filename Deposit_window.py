from tkinter import Toplevel, StringVar, Label, Button, Entry
from bank_system import Bank_system
from Assets_window import Assets_window

class Deposit_window:
    def start_deposit_window(self, home_screen, account_id, username):
        self.account_id = account_id
        self.deposit_window = Toplevel(home_screen)
        self.deposit_window.geometry('400x125')
        self.deposit_window.title('Deposit [{}]'.format(username))

        self.temp_deposit_value = StringVar()
        
        #Labels
        details_label = Label(self.deposit_window, text = 'How much do you want to deposit?', font=('Calibri',20))
        details_label.grid(row=0, column=0, sticky='N')

        amount_lable = Label(self.deposit_window, text = 'Amount', font=('Calibri',16))
        amount_lable.grid(row=1, column=0, sticky='W')

        #hidden label
        self.hidden_label = Label(self.deposit_window, font=('Calibri',12))
        self.hidden_label.grid(row=4, sticky='N')

        #Entries
        self.deposit_entry = Entry(self.deposit_window, textvariable=self.temp_deposit_value)
        self.deposit_entry.grid(row=1, column=0)

        #Buttons
        ok_button = Button(self.deposit_window, text='Ok', font=('Calibri', 16), width=10,command=lambda: self.start_deposit())
        ok_button.grid(row=2, column=0, sticky='E')

        go_back_button = Button(self.deposit_window, text='Go back', font=('Calibri', 16), width=10,command=lambda: self.deposit_window.destroy())
        go_back_button.grid(row=2, column=0, sticky='W', padx=5)
        #Note to self, add function to close all windows on logout

    def start_deposit(self):
        amount = self.temp_deposit_value.get()
        if(self.check_user_input(amount)):
            self.finish_deposit(amount)
        
    def finish_deposit(self, amount):            
        Bank_system().deposit(self.account_id, amount)
        self.deposit_entry.delete(0, 'end')
        self.deposit_window.geometry('400x150')
        self.hidden_label.config(fg='green',text='The deposit was successfully made')
        #Note to self, add function to check if the deposit was succesful

    def check_user_input(self, amount):
        lower_bound = '150'
        horozontal_bound = '400'
        if(" " in amount):
            self.deposit_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.hidden_label.config(fg='red',text='Spaces are not allowed')
            return False
        elif(amount == ''):
            self.deposit_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.hidden_label.config(fg='red',text='Please enter the amount')
            return False
        elif(not(amount.isdecimal())):
            self.deposit_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.hidden_label.config(fg='red',text='The ammount has to be given in numbers')
            return False
        else:
            self.deposit_window.geometry('{}x{}'.format(horozontal_bound, lower_bound))
            self.hidden_label.config(fg='red',text='')
            return True