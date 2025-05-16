from customtkinter import *
from tkinter import *
import mouse
import time
import keyboard
import threading

isClicking = False
keyboardCheck = False
button1 = 'left'
speed = 1
y = ''
delay = 5
interval1 = 5


def check_entry(*args):
    if entry_var.get():
        global keyboardCheck

        radiobutton_1_LEFT.configure(state="disabled", fg_color='gray')
        radiobutton_3_RIGHT.configure(state="disabled", fg_color='gray')
        radiobutton_2_MIDDLE.configure(state="disabled", fg_color='gray')
        keyboardCheck = True

    else:
        radiobutton_1_LEFT.configure(state="normal", fg_color='white')
        radiobutton_3_RIGHT.configure(state="normal", fg_color='white')
        radiobutton_2_MIDDLE.configure(state="normal", fg_color='white')
        keyboardCheck = False

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
    print(entry.get())

def actual_information():
    global speed
    global button1
    global interval1
    global y
    Letter = entry_var.get()
    Letter_mouse = radio_var.get()
    Speed = entry1.get()
    y = str(entry_var.get())

    button_Save.configure(fg_color='#287233', hover_color='#287233')

    interval1 = int(entry2.get())

    if keyboardCheck:
        label_Choiced_Button.configure(text=f"Выбранная кнопка: {Letter}")
    else:
        label_Choiced_Button.configure(text=f"Выбранная кнопка: {Letter_mouse}")
        button1 = Letter_mouse

    if ',' in str(Speed):
        Speed = float(str(Speed).replace(',', '.'))
        speed = Speed
        label_Choiced_Speed.configure(text=f"Текущая скорость нажатия: {Speed}")
    if str(Speed) =='':
        speed = 1
        label_Choiced_Speed.configure(text=f"Текущая скорость нажатия: {speed}")
    else:
        speed = float(Speed)
        label_Choiced_Speed.configure(text=f"Текущая скорость нажатия: {Speed}")






    print(f'Кнопка {Letter}, Скорость {Speed}, Проверка клавы {keyboardCheck}, переменная y = {y}, mouse {button1}')

def set_clicker_bind():
    global isClicking
    if isClicking:
        isClicking = False
        print('Авто-кликер: Off')
        label_ON_OFF.configure(text="Автокликер: Выключен")
        button_Start.configure(fg_color='#9b2d30', hover_color='#287233')
    else:
        isClicking = True
        print('Авто-Кликер: On')
        label_ON_OFF.configure(text="Автокликер: Включен")
        button_Start.configure(fg_color='#287233', hover_color='#9b2d30')
        if keyboardCheck:
            threading.Thread(target=keyboard_clicker, daemon=True).start()
        else:
            threading.Thread(target=mouse_clicker, daemon=True).start()

def set_clicker():
    global isClicking
    global interval
    if isClicking:
        isClicking = False
        print('Авто-кликер: Выкл')
        label_ON_OFF.configure(text="Автокликер: Выключен")
        button_Start.configure(fg_color='#9b2d30', hover_color='#287233')
    else:
        isClicking = True
        print('Авто-Кликер: Вкл')
        label_ON_OFF.configure(text="Автокликер: Включен")
        button_Start.configure(fg_color='#287233', hover_color='#9b2d30')
        if keyboardCheck:
            threading.Timer(interval1, lambda: threading.Thread(target=keyboard_clicker, daemon=True).start()).start()
        else:
            threading.Timer(interval1, lambda: threading.Thread(target=mouse_clicker, daemon=True).start()).start()

def mouse_clicker():
    global isClicking
    while isClicking:
        mouse.double_click(button=button1)
        time.sleep(float(speed))

def keyboard_clicker():
    global isClicking
    while isClicking:
        keyboard.send(y)
        time.sleep(float(speed))

def close_window(event=None):
    window.destroy()

def Save_but_color_need_saving(*args):
    button_Save.configure(fg_color='#9b2d30', hover_color='#287233')

    #button_Save.configure(fg_color='#287233', hover_color='#9b2d30')

timer_mouse = threading.Timer(delay, mouse_clicker )
timer_keyboard = threading.Timer(delay, keyboard_clicker )

window = CTk()
window.title('Auto Clicker - 5')
window.geometry('500x500')
set_appearance_mode("dark")
window.eval('tk::PlaceWindow . center')

window.grid_columnconfigure((0, 1, 2), weight=1)
window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

keyboard.add_hotkey('F1', set_clicker_bind)
window.bind('<F2>', close_window)

frame_RIGHT_Choice = CTkFrame(window)
frame_RIGHT_Choice.pack(side="right", anchor="n", padx=20, pady=20)

frame_RIGHT_Bottom = CTkFrame(window)
frame_RIGHT_Bottom.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)

frame_LEFT = CTkFrame(window)
frame_LEFT.pack(side="left", anchor="nw", padx=20, pady=20)

frame_LEFT_BOTTOM = CTkFrame(window)
frame_LEFT_BOTTOM.place(relx=0.0, rely=1.0, anchor='sw', x = 20, y = -20)


radio_var = StringVar(value='left')
radiobutton_1_LEFT = CTkRadioButton(frame_RIGHT_Choice, text="Выбрать: ЛКМ",
                                    command=radiobutton_event, variable=radio_var, value='left', fg_color='white')
radiobutton_2_MIDDLE = CTkRadioButton(frame_RIGHT_Choice, text="Выбрать: ПКМ",
                                      command=radiobutton_event, variable=radio_var, value='right', fg_color='white')
radiobutton_3_RIGHT = CTkRadioButton(frame_RIGHT_Choice, text="Выбрать: СКМ",
                                     command=radiobutton_event, variable=radio_var, value='middle', fg_color='white')

radiobutton_1_LEFT.pack(pady=10)
radiobutton_2_MIDDLE.pack(pady=10)
radiobutton_3_RIGHT.pack(pady=10)

entry_var = StringVar()
entry_var.trace_add("write", check_entry)
entry_var.trace_add("write", Save_but_color_need_saving)

label = CTkLabel(frame_RIGHT_Choice, text='Клавиша клавиатуры')
label.pack(pady=0)
entry = CTkEntry(frame_RIGHT_Choice, textvariable=entry_var, placeholder_text="Кнопка")
entry.pack(pady=0)


entry_var_Speed = StringVar(value=1)
entry_var_Speed.trace_add("write", Save_but_color_need_saving)

label = CTkLabel(frame_RIGHT_Choice, text='Скорость нажатия')
label.pack(pady=0, anchor="center")
entry1 = CTkEntry(frame_RIGHT_Choice, textvariable=entry_var_Speed)
entry1.pack(pady=0, anchor="center")


entry_var_Time = StringVar(value=5)
entry_var_Time.trace_add("write", Save_but_color_need_saving)

label = CTkLabel(frame_RIGHT_Choice, text='Время для включения')
label.pack(pady=0, anchor="center")
entry2 = CTkEntry(frame_RIGHT_Choice, textvariable=entry_var_Time , placeholder_text="")
entry2.pack(pady=0, anchor="center")



button_Save = CTkButton(frame_RIGHT_Bottom, text='Сохранить', command=actual_information, fg_color='#9b2d30',hover_color='#287233' )
button_Save.pack(pady=10)

button_Start = CTkButton(frame_RIGHT_Bottom, text='ВКЛ/ВЫКЛ', command=set_clicker, fg_color='#9b2d30', hover_color='#287233')
button_Start.pack(pady=10)

label_Choiced_Button = CTkLabel(frame_LEFT, text='Выбранная кнопка: left')
label_Choiced_Button.pack(pady=5, anchor="w")
label_Choiced_Speed = CTkLabel(frame_LEFT, text='Текущая скорость нажатия: 1')
label_Choiced_Speed.pack(pady=5, anchor="w")

label_ON_OFF = CTkLabel(frame_LEFT, text = 'Автокликер: Выключен')
label_ON_OFF.pack(pady=5, anchor="w")

label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = '<Добро пожаловать в Auto Clicker Версия 5>')
label_left_bottom.pack(anchor="w")
label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = '• F1 - Включить кликер без задержки')
label_left_bottom.pack(padx=15 , anchor="w")
label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = '• F2 - Закрыть программу')
label_left_bottom.pack(padx=15 , anchor="w")
label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = '• Клавиша клавиатуры: англ. буквы\n  или англ. обозначения (TAB, SPACE) ',justify="left")
label_left_bottom.pack(padx=15, anchor="w")
label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = '• Скорость нажатия: Пример 0.25')
label_left_bottom.pack(padx=15 , anchor="w")
label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = '• Время для включения: Сколько секунд\n  пройдет перед включением. \n (только для кнопки "ВКЛ/ВЫКЛ)', justify="left")
label_left_bottom.pack(padx=15, anchor="w")
label_left_bottom = CTkLabel(frame_LEFT_BOTTOM,text = 'Сделал Bob_stroitel',justify="right")
label_left_bottom.pack(padx=15, anchor="e")




window.mainloop()
