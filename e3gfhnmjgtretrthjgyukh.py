
from customtkinter import *

window = CTk()
window.title('Swine')
window.geometry('400x300')


values=('left', 'middle', 'right')

mouseChoice = StringVar()

title = CTkLabel(window,text='g', fg_color='Gray80', corner_radius=0)
title.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

for i in range(len(values)):
    radiobutton = CTkRadioButton(window,text=values[i], value=values[i], variable = mouseChoice)
    radiobutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky='w')

fgeg = mouseChoice.get()
print (fgeg)

window.mainloop()