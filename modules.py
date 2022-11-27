from tkinter import *
import threading
import time

def dialogue(text, cmd, continue_text="Дальше", color="green"):
    label_desc = Label(text=text,
                       font=('Arial', 22), bg='black', fg=color)
    label_desc.place(x=50, y=100, width=500, height=400)

    continue_button = Button(text=continue_text, command=cmd,
                             font=('Arial', 19),
                             fg=color, bg='black')
    continue_button.place(x=40, y=450, width=200, height=70)


def btn_blink(button, first_color, second_color, delay=1):
    def blink():
        counter = 0
        while button.winfo_exists():
            if counter % 2 == 0:
                button.configure(bg=first_color)
            else:
                button.configure(bg=second_color)
            time.sleep(delay)
            counter += 1
    t1 = threading.Thread(target=blink)
    t1.start()