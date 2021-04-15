from tkinter import Toplevel, Label, Button 
from bank_system import Bank_system

class Assets_window:
    def start_assets_window(self, home_screen, account_id, username):
        self.home_screen = home_screen
        self.account_id = account_id
        self.username = username
        self.update_assets_window()

    def update_assets_window(self):
        self.assets_window = Toplevel(self.home_screen)
        self.assets_window.geometry('300x110')
        self.assets_window.title('Assets [{}]'.format(self.username))
    
        assets = self.get_assets()
        #Labels
        self.details_label = Label(self.assets_window, text = 'Your assets are: {}.00$'.format(assets), font=('Calibri',20))
        self.details_label.grid(row=0, column=0, sticky='N')

        #Buttons
        go_back_button = Button(self.assets_window, text='Go back', font=('Calibri', 16), width=10,command=lambda: self.assets_window.destroy())
        go_back_button.grid(row=1, column=0, sticky='W', padx=5)

        update_button = Button(self.assets_window, text='Update', font=('Calibri', 16), width=10,command=lambda: self.update_assets())
        update_button.grid(row=1, column=0, sticky='E', pady=5)

    def get_assets(self):
        print('assets window',self.account_id)
        return Bank_system().get_assets(self.account_id)
    
    def update_assets(self):
        self.assets_window.destroy()
        self.start_assets_window(self.home_screen, self.account_id, self.username)

