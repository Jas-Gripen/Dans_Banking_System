from tkinter import Toplevel, Label, Button 
class Exit_window:
    def exit_program(self, home_screen):
        self.exit_window = Toplevel(home_screen)
        self.exit_window.geometry('400x150')
        self.exit_window.title('Exit')
        title_lable = Label(self.exit_window, text = 'Are you sure you want to exit the program?', font=('Calibri',16))
        title_lable.grid(row=0, column=0, sticky='N')

        #Buttons
        yes_button = Button(self.exit_window, width=10, text='yes', font=('Calibri', 16), command=lambda: quit())
        yes_button.grid(row=1, column=0, sticky='N')

        no_button = Button(self.exit_window, width=10, text='no', font=('Calibri', 16), command=lambda: self.exit_window.destroy())
        no_button.grid(row=2, column=0, sticky='N', pady=5)