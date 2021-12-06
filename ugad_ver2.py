from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import random

def new_game():
    global answers, comp_number
    comp_number = random.randint(1, 100)
    answers.delete(0, END)

def click_button():
    global answers
    try:
        user_number = int(number.get())
        print(user_number + 1)
        if user_number < comp_number:
            answers.insert(0,  " ������ " + str(user_number))
        elif user_number > comp_number:
            answers.insert(0, " ������ " + str(user_number))
        else:
            messagebox.showinfo("����������", "������!")
            new_game()
            
    except:
        messagebox.showinfo("������", "������� �����!")




win = Tk()
win.title("��������")
win.geometry('600x350')
big_font = font.Font(size=30)

label = Label(text="� ������� ����� �� 1 �� 100", font=big_font)
label.place(x=10, y=10)

number = Entry(font=big_font, width=5)
number.place(x=10, y=100)

button = Button(text="�����������", font=big_font, command=click_button)
button.place(x=10, y=170)

answers = Listbox(font=big_font, width=10, heigh=5)
answers.place(x=300, y=100)

new_game()

win.mainloop()
