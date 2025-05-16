import mouse
import time
import keyboard
from tkinter import *

window = Tk()
window.title('Auto_Clicker_4') # Имя
window.geometry('800x800') #Размер

def param():
    param1 = Message(text = f'')

label = Label(text='=====   Установленные параметры   =====', font =('Times Mew Roman',20))
label.place(x=110,y=0)
label.configure(justify=CENTER)




label = Label(text='=====   Ввод параметров   =====', font =('Times Mew Roman',20))
label.place(x=170,y=400)
label.configure(justify=CENTER)

name = Entry(width=30) # Entry - ввод данных в строчку
name.place(x=75,y=155)

about = Message(text=f'скорость {name} \n'
                     f'Кнопка', font = ('Times New Roman', 15))
about.place(x=25, y=70)





















window.mainloop()