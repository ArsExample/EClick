from tkinter import *
import time
import random

window = Tk()
window.geometry('700x600')
window.title('Clicker from Evandiy')
clicks = 0


def hacked_menu2():
    label_fg = Label(bg='black')
    label_fg.place(x=0, y=0, width=700, height=600)

    label_title = Label(text='Как тут все плохо...', font=('Arial', 20), bg='black', fg='red')
    label_title.place(x=200, y=0, width=300, height=90)

    label_title1 = Label(text='Давай для начала починим цвет кнопок', font=('Arial', 20), bg='black', fg='red')
    label_title1.place(x=0, y=80, width=700, height=90)

    hacked_button1 = Button(text='Начать $*@_', font=('Arial', 22), bg='red', fg='black')
    hacked_button1.place(x=250, y=150, width=200, height=70)

    hacked_button2 = Button(text='+@ игре', font=('Arial', 22), bg='red', fg='black')
    hacked_button2.place(x=250, y=270, width=200, height=70)

    hacked_button3 = Button(text='Выйти #* (гры', font=('Arial', 22), bg='red', fg='black')
    hacked_button3.place(x=250, y=390, width=200, height=70)

    def change_text():
        hacked_button1['text'] = 'Начать игру'
        hacked_button2['text'] = 'Об игре'
        hacked_button3['text'] = 'Выйти из игры'
        help_but['text'] = 'Продолжить'
        help_but['bg'] = 'yellow'
        help_but['command'] = goodbay

    def goodbay():
        label_title['text'] = 'Cпасибо за помощь!'
        label_title1['text'] = 'Я пойду делать игру дальше и фиксить баги'

        hacked_button1['text'] = 'Надеюсь'

        hacked_button2['text'] = 'Еще'

        hacked_button3['text'] = 'Увидимся!'

        help_but['text'] = 'Закончить игру'
        help_but['bg'] = 'yellow'
        help_but['command'] = leave_game

    def change_but():
        hacked_button1['bg'] = 'purple'
        hacked_button2['bg'] = 'purple'
        hacked_button3['bg'] = 'purple'
        label_title['text'] = 'Класс!'
        label_title['fg'] = 'orange'
        label_title1['text'] = 'Теперь надо вернуть правильный текст...'
        label_title1['fg'] = 'orange'
        help_but['text'] = 'Починить текст'
        help_but['command'] = change_text

    help_but = Button(text='Починить цвет', command=change_but, font=('Arial', 22), bg='lime', fg='black')
    help_but.place(x=200, y=510, width=300, height=80)


def void():
    label_fg = Label(bg='black')
    label_fg.place(x=0, y=0, width=700, height=600)
    label_title = Label(text='. . .', font=('Arial', 40), bg='black', fg='red')
    label_title.place(x=0, y=0, width=700, height=90)


def start_hacked_game():
    def changes_color():
        label_fg = Label(bg='black')
        label_fg.place(x=0, y=0, width=700, height=600)

        label_title = Label(text='Ура! Так намного лучше)', font=('Arial', 22), bg='black', fg='orange')
        label_title.place(x=0, y=100, width=700, height=90)

        label_title1 = Label(text='Теперь пойдем починим главное меню!', font=('Arial', 22), bg='black', fg='orange')
        label_title1.place(x=0, y=200, width=700, height=90)

        help_but = Button(text='Починить цвет', command=changes_color, font=('Arial', 22), bg='lime', fg='black')
        help_but.destroy()

        cont_button = Button(text='В главное меню', command=hacked_menu2, font=('Arial', 22), bg='white', fg='black')
        cont_button.place(x=200, y=400, width=300, height=80)

    def thank():
        label_fg = Label(bg='black')
        label_fg.place(x=0, y=0, width=700, height=600)
        label_title = Label(text='Спасибо! Просто...', font=('Arial', 22), bg='black', fg='red')
        label_title.place(x=0, y=0, width=700, height=90)

        label_title2 = Label(text='Я ведь текст на экране', font=('Arial', 22), bg='black', fg='red')
        label_title2.place(x=0, y=100, width=700, height=90)

        label_title2 = Label(text='У меня нет рук и я не могу жать на кнопки:(', font=('Arial', 22), bg='black',
                             fg='red')
        label_title2.place(x=0, y=200, width=700, height=90)

        help_but = Button(text='Починить цвет', command=changes_color, font=('Arial', 22), bg='lime', fg='black')
        help_but.place(x=200, y=400, width=300, height=80)

    def quethion():
        label_fg = Label(bg='black')
        label_fg.place(x=0, y=0, width=700, height=600)

        label_title = Label(text='Ох, кажется игра сломалась...', font=('Arial', 22), bg='black', fg='red')
        label_title.place(x=0, y=0, width=700, height=90)

        label_title2 = Label(text='Поможешь мне починить её??', font=('Arial', 22), bg='black', fg='red')
        label_title2.place(x=0, y=200, width=700, height=90)

        yes_but = Button(text='Да', command=thank, font=('Arial', 22), bg='black', fg='red')
        yes_but.place(x=120, y=450, width=200, height=80)
        no_but = Button(text='Нет', command=void, font=('Arial', 22), bg='black', fg='red')
        no_but.place(x=370, y=450, width=200, height=80)

        # help_but = Button(text = 'Починить игру', command = changes, font = ('Arial', 22), bg = 'lime', fg = 'black')
        # help_but.place(x = 200, y = 500, width = 300, height = 80)

    quethion()


def hacked_description_game():
    label_title = Label(text='%;№;"*(№()№', font=('Arial', 40), bg='black', fg='red')
    label_title.place(x=200, y=0, width=500, height=90)

    continue_button = Button(text='В главное меню', command=hacked_menu, font=('Arial', 19), fg='red', bg='black')
    continue_button.place(x=40, y=450, width=200, height=70)


def dont_leave_game():
    label_title = Label(text='Не удалось совершить действие', font=('Arial', 30), bg='black', fg='red')
    label_title.place(x=0, y=0, width=700, height=90)


def hacked_menu():
    label_fg = Label(bg='black')
    label_fg.place(x=0, y=0, width=700, height=600)

    label_title = Label(text='ERROR', font=('Arial', 40), bg='black', fg='red')
    label_title.place(x=200, y=0, width=300, height=90)

    hacked_button1 = Button(text='Начать $*@_', command=start_hacked_game, font=('Arial', 22), bg='red', fg='black')
    hacked_button1.place(x=250, y=150, width=200, height=70)

    hacked_button2 = Button(text='+@ игре', command=hacked_description_game, font=('Arial', 22), bg='red', fg='black')
    hacked_button2.place(x=250, y=270, width=200, height=70)

    hacked_button3 = Button(text='Выйти #* (гры', command=dont_leave_game, font=('Arial', 22), bg='red', fg='black')
    hacked_button3.place(x=250, y=390, width=200, height=70)


def start_game():
    label_fg = Label(bg='black')
    label_fg.place(x=0, y=0, width=700, height=600)

    label_quethion = Label(text='Привет! Дать тебе кнопку?',
                           font=('Arial', 22),
                           bg='black', fg='orange')
    label_quethion.place(x=150, y=0, width=400, height=90)

    def yes_answer():
        label_answ = Label(text='Ну ладно, держи)',
                           font=('Arial', 20),
                           bg='black', fg='orange')
        label_answ.place(x=120, y=0, width=450, height=90)
        yes_but.destroy()
        no_but.destroy()

        red_but = Button(bg='red', command=first_task)
        red_but.place(x=220, y=200, width=250, height=250)

    def no_answer():
        label_answ = Label(text='У тебя нет выбора (-_-)',
                           font=('Arial', 20),
                           bg='black', fg='orange')
        label_answ.place(x=150, y=0, width=400, height=90)
        yes_but.destroy()
        no_but.destroy()

        red_but = Button(bg='red', command=first_task)
        red_but.place(x=220, y=200, width=250, height=250)

    yes_but = Button(text='Да', command=yes_answer,
                     font=('Arial', 22),
                     bg='black', fg='red')
    yes_but.place(x=120, y=200, width=200, height=80)

    no_but = Button(text='Нет', command=no_answer,
                    font=('Arial', 22),
                    bg='black', fg='red')
    no_but.place(x=370, y=200, width=200, height=80)

    def first_task():
        global clicks
        clicks += 1
        points = Label(text=str(clicks), font=('Arial', 17), bg='black', fg='white')
        points.place(x=0, y=0, width=30, height=30)
        label_answ = Label(text='Нажми на эту кнопку 30 раз!',
                           font=('Arial', 20),
                           bg='black', fg='orange')
        label_answ.place(x=150, y=0, width=400, height=90)
        if clicks >= 30:
            label1 = Label(text='Молодец! А сможешь нажать на неё 50 раз?',
                           font=('Arial', 20),
                           bg='black', fg='orange')
            label1.place(x=90, y=0, width=570, height=90)
            clicks2 = clicks - 30
            points['text'] = str(clicks2)
            yellow_but = Button(text='Тык', font=('Arial', 24), bg='yellow', command=first_task)
            yellow_but.place(x=220, y=200, width=250, height=250)

        if clicks >= 80:
            label1 = Label(text='Здорово! Вот тебе еще одна кнопка! :)', font=('Arial', 20), bg='black', fg='orange')
            label1.place(x=90, y=0, width=570, height=90)

            def hack_clear():
                label1.forget()
                but1.destroy()
                yes_but.destroy()
                no_but.destroy()

            def hack():
                hack_clear()
                for i in range(100):
                    leave_button = Button(text='ERROR', command=hack_clear, font=('Arial', 22), bg='red', fg='black')
                    leave_button.place(x=random.randint(1, 550), y=random.randint(1, 550), width=300, height=70)

            but1 = Button(text='Не жми на меня!', command=hack, font=('Arial', 13), bg='black', fg='red')
            but1.place(x=500, y=450, width=150, height=70)

            window.protocol('WM_DELETE_WINDOW', hacked_menu)


def description_game():
    label_text = Label(text='Об игре:',
                       font=('Arial', 40),
                       bg='black', fg='orange')
    label_text.place(x=200, y=0, width=300, height=90)

    def words7():
        label_desc = Label(text='made by Evandiy',
                           font=('Arial', 22), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='В главное меню', command=main_menu,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    def words6():
        label_desc = Label(text='В игре наверняка будет куча ошибок)',
                           font=('Arial', 20), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='Дальше', command=words7,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    def words5():
        label_desc = Label(text='Я еще только учусь, поэтому...',
                           font=('Arial', 19), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='Дальше', command=words6,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    def words4():
        label_desc = Label(text='Следуй указаниям и у тебя все получится!',
                           font=('Arial', 19), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='Дальше', command=words5,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    def words3():
        label_desc = Label(text='Управление в игре только мышкой.',
                           font=('Arial', 22), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='Дальше', command=words4,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    def words2():
        label_desc = Label(text='Вы запустили мой кликер)',
                           font=('Arial', 22), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='Дальше', command=words3,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    def words1():
        label_desc = Label(text='Привет, это я, создатель игры.',
                           font=('Arial', 22), bg='black', fg='green')
        label_desc.place(x=50, y=100, width=500, height=400)
        continue_button = Button(text='Дальше', command=words2,
                                 font=('Arial', 19),
                                 fg='red', bg='black')
        continue_button.place(x=40, y=450, width=200, height=70)

    words1()


def leave_game():
    window.quit()


def main_menu():
    label_fg = Label(bg='black')
    label_fg.place(x=0, y=0, width=700, height=600)
    label_title = Label(text='EClick',
                        font=('Arial', 40),
                        bg='black', fg='orange')
    label_title.place(x=200, y=0, width=300, height=90)

    first_button = Button(text='Начать игру', command=start_game,
                          font=('Arial', 22),
                          bg='purple', fg='black')
    first_button.place(x=250, y=150, width=200, height=70)

    second_button = Button(text='Об игре', command=description_game,
                           font=('Arial', 22),
                           bg='purple', fg='black')
    second_button.place(x=250, y=270, width=200, height=70)

    third_button = Button(text='Выйти из игры', command=leave_game,
                          font=('Arial', 22),
                          bg='purple', fg='black')
    third_button.place(x=250, y=390, width=200, height=70)


main_menu()

window.mainloop()
