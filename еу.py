from customtkinter import *

class mainwindow(CTk):
    def __init__(self):
        super().__init__()
        self.title('имя')
        self.geometry('600x500')

        self.grid_columnconfigure((0,1,2), weight = 1)
        self.grid_rowconfigure((0, 1, 2, 3,4,5,6,7,8,9,10), weight = 1)

        self.button = CTkButton(self, text='Подтвердить', command=self.accept)
        self.button.grid(row=1, padx=10, pady=10, sticky='ew', columnspan=2)

        self.text=CTkLabel(self, text='')
        self.text.grid(row=2, padx=10, pady=10, sticky='ew', columnspan=2)
        self.text.configure(size=20)

            #checkbox panel
        #self.checkboxes = ChekboxFrame(self, title = 'Выбери цвет', values=('Жёлтый', 'Чёрный', 'Синий'))
        #self.checkboxes.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
            #radiobutton panel
        self.radiobutton = RadiobuttonFrame(self, title='Выбор кнопки мыши: ', values=('left', 'middle', 'right'))
        self.radiobutton.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')


    def accept(self):
        self.text.configure(text=f"Скорость нажатия:  \n Выбранная клавиша мыши: {self.radiobutton.get()}")

class RadiobuttonFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.figure = StringVar()
        self.title = CTkLabel(self, text=title, fg_color='Gray80', corner_radius=0)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        for i in range(len(values)):
            radiobutton = CTkRadioButton(self, text=values[i], value=values[i], variable = self.figure)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky='w')


    def get(self):
        return self.figure.get()

window = mainwindow()


window.mainloop()

root.mainloop()
