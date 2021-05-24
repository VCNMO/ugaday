import tkinter as tk
from tkinter import messagebox
import random


def check_number():
    global step
    # print(text_enter.get())

    try:
        user_number = int(text_enter.get())
        step += 1
    except:
        user_number = 0

    text_steps.config(text="Шагов: " + str(step))
    if user_number > number:
        text_answer.config(text="меньше")
    elif user_number < number:
        text_answer.config(text="больше")
    else:
        messagebox.showinfo("Информация", "Угадал!")
        new_game()

def new_game():
    global number, step
    number = new_number()
    step = 0
    text_steps.config(text="Шагов: 0")
    text_answer.config(text="")
    text_enter.delete(0, len(text_enter.get()))

def test():
    text_enter.delete(0, len(text_enter.get()))

def new_number():
    return random.randrange(1, 101)



win = tk.Tk()
win.geometry("600x400")
win.title("Угадай число!")
win.configure(background="")

title = tk.Label(text="УГАДАЙ ЧИСЛО", font='Times 30', foreground="#ffcc00")
title.pack()
text_invite = tk.Label(text="Я загадал число от 1 до 100. Угадай!")
text_invite.pack()

text_enter = tk.Entry()
text_enter.pack()

button_check = tk.Button(text="Проверить", command=check_number, background="#aaaaff")
#button_check.pack()
button_check.place(x=100, y=200)

# button_check = tk.Button(text="Проверить", command=test)
# button_check.pack()

text_answer = tk.Label()
text_answer.pack()

text_steps = tk.Label(text="Шагов: 0")
text_steps.pack()
new_game()

win.mainloop()