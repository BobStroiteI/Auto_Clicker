import mouse
import time
import keyboard


isClicking = False
keyboardCheck = False
button1 = 'left'
speed = 1
y = ''


def set_clicker():
    global isClicking

    if isClicking:
        isClicking = False
        print('Авто-кликер: Off')
    else:
        isClicking = True
        print('Авто-Кликер: On')
def button():
    global button1
    global speed
    global y
    global keyboardCheck

    x = int(input('1 - Левая кнопка мыши \n'
                  '2 - Колёсико мыши \n'
                  '3 - Правая кнопка мыши \n'
                  '4 - Выбрать клавишу клавиатуры \n'
                  '5 - Выбрать скорость нажатия \n'
                  ''
                  ))
    if x == 1:
        print ('Выбрано: Левая кнопка мыши')
        button1 = 'left'
    elif x == 2:
        print('Выбрано: Колёсико мыши')
        button1 = 'middle'
    elif x == 3:
        button1 = 'right'
        print('Выбрано: Правая кнопка мыши')
    elif x == 4:
        y = str(input('Выберите нужную клавишу (на англ. раскладке)'))
        print(f'Выбранная клавиша: {y}')
        keyboardCheck = True
    elif x == 5:
        speed = (input('Выберите скорость нажатия (Пример: 0.01)\n'
                       ''))
        print (f'Выбранная скорость: {speed}')



keyboard.add_hotkey('] + [', set_clicker)
keyboard.add_hotkey('[ + p', button)


print ('Добро пожаловать в "АвтоКликерВерсия4" его сделал я Bob_stroitel \n'
       '1) Для работы нужно переключить язык на англ. \n'
       '2) Комбинации клавиш: ] + [  -  Вкл/выкл, [ + p  -  Выбрать клавиши или скорость \n'
       f'3) Параметры по умолчанию: Скорость - {speed}, Клавиша мыши - {button1} '
       ''
)

while keyboardCheck == False:
    while True:
        if isClicking == True:
            mouse.double_click(button = button1)
            time.sleep(float(speed))
            if keyboardCheck == True:
                break

while keyboardCheck == True:
    while True:
        if isClicking == True:
            keyboard.send(y)
            time.sleep(float(speed))
            if keyboardCheck == False:
                break
