from tkinter import Toplevel, StringVar, Label, Button, Entry 
from bank_system import Bank_system
from Assets_window import Assets_window

class Withdraw_window:
    def start_withdraw_window(self, home_screen, account_id, username):
        self.account_id = account_id
        self.withdraw_window = Toplevel(home_screen)
        self.withdraw_window.geometry('420x125')
        self.withdraw_window.title('withdraw [{}]'.format(username))

        self.temp_withdraw_value = StringVar()
        
        #Labels
        details_label = Label(self.withdraw_window, text = 'How much do you want to withdraw?', font=('Calibri',20))
        details_label.grid(row=0, column=0, sticky='N')

        amount_lable = Label(self.withdraw_window, text = 'Amount', font=('Calibri',16))
        amount_lable.grid(row=1, column=0, sticky='W')

        #hidden label
        self.hidden_label = Label(self.withdraw_window, font=('Calibri',12))
        self.hidden_label.grid(row=4, sticky='N')

        #Entries
        self.withdraw_entry = Entry(self.withdraw_window, textvariable=self.temp_withdraw_value)
        self.withdraw_entry.grid(row=1, column=0)

        #Buttons
        ok_button = Button(self.withdraw_window, text='Ok', font=('Calibri', 16), width=10,command=lambda: self.withdraw())
        ok_button.grid(row=2, column=0, sticky='E')

        go_back_button = Button(self.withdraw_window, text='Go back', font=('Calibri', 16), width=10,command=lambda: self.withdraw_window.destroy())
        go_back_button.grid(row=2, column=0, sticky='W', padx=5)
        #Note to self, add function to close all windows on logout

    def withdraw(self):
        ammount = self.temp_withdraw_value.get()
        Bank_system().withdraw(self.account_id, ammount)
        self.withdraw_entry.delete(0, 'end')
        self.withdraw_window.geometry('420x150')
        self.hidden_label.config(fg='green',text='The withdraw was successfull')
        #Note to self, add function to check if the withdraw was succesful