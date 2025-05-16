from tkinter import *

window = Tk()
window.title('Swin 1.0') # Имя
window.geometry('700x500') #Размер

def check():
    print(name.get(), selected_gender.get(), age.get(), check_state.get())
    label.configure(text=f'Привет, {name.get()}') #Меняет текст нашего label если нажать кнопку отправить




label = Label(text='Расскажите о себе', font =('arial',20)) #  Label - одна строка
label.place(x=200,y=10) # Верхний левый угол - x0 y0

about = Message(text='Добро пожаловать в наше замечательное приложение. Пожалуйста, ответьте на вопросы (только честно!), вся информация будет между нами.', font=('Arial', 14), width=680)
about.configure(justify=CENTER) # выравнивание, Massage - Текст
about.place(x=25, y=70)

name = Entry(width=30) # Entry - ввод данных в строчку
name.place(x=75,y=155)
label_name = Label(text='ФИО:', font=('Arial', 15))
label_name.place(x=5,y=150)

selected_gender = IntVar() # Записать значения
rad1 = Radiobutton(text='муж', value = 1, variable=selected_gender) #Кнопочка выбора - Radiobutton
rad2 = Radiobutton(text = 'жен', value = 2,variable=selected_gender) # value - знач. variable - куда записывается
rad1.place(x=10,y=200 )
rad2.place(x=100,y=200)

label_age = Label(text='Сколько лет', font=('Arial', 15))
label_age.place(x=5, y=250)
age = Spinbox(from_= 0 , to=100, width = 20) # Spinbox - выбор с поомщью стрелочек, !!! у front_ есть "_"
age.place(x=10,y=300)

check_state = IntVar()
check_btn = Checkbutton(text='Запомнить меня', variable = check_state)
check_btn.place(x=10, y=350)

btn = Button(text='Отправить', font=('Arial',15), command=check)  # Создание кнопки, command - запуск функции
btn.place(x=10,y=400)





window.mainloop() #Запускает обработку событий связанных с окном (писать в конце программы)