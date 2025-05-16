from customtkinter import *

class mainwindow(CTk):
    def __init__(self):
        super().__init__()
        self.title('имя')
        self.geometry('600x500')

        self.grid_columnconfigure((0,1), weight = 1)
        self.grid_rowconfigure((0,1,2), weight = 1)

        self.button = CTkButton(self, text='Отправить', command=self.show_info)
        self.button.grid(row=1, padx=10, pady=10, sticky='ew', columnspan=2)

        self.text=CTkLabel(self, text='')
        self.text.grid(row=2, padx=10, pady=10, sticky='ew', columnspan=2)

        #checkbox panel
        self.checkboxes = ChekboxFrame(self, title = 'Выбери цвет', values=('Жёлтый', 'Чёрный', 'Синий'))
        self.checkboxes.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        #radiobutton panel
        self.radiobutton = RadiobuttonFrame(self, title='Выбери фигуру', values=('Круг', 'Квадрат', 'Овал'))
        self.radiobutton.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
    def show_info(self):
        self.text.configure(text=f"цвет: {self.checkboxes.get()} \n Фигура {self.radiobutton.get()}")
class ChekboxFrame(CTkFrame): # master - тот объект в который кладём наш Frame
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight = 1)
        self.checkboxes=[]
        self.title = CTkLabel(self, text=title, fg_color='grey30', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        for i in range(len(values)):
            checkbox = CTkCheckBox(self, text=values[i])
            checkbox.grid(row=i+1, column = 0, padx=10,pady=10, sticky='w')
            self.checkboxes.append(checkbox)
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get()==1:
                checked_checkboxes.append(checkbox.cget('text'))
        return ', '.join(checked_checkboxes)



class RadiobuttonFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.figure = StringVar()
        self.title = CTkLabel(self, text=title, fg_color='Red', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        for i in range(len(values)):
            radiobutton = CTkRadioButton(self, text=values[i], value=values[i], variable = self.figure)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky='w')


    def get(self):
        return self.figure.get()

window= mainwindow()
window.mainloop()