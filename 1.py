#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

def calculate(event):
    n1 = first_number.get()
    n2 = second_number.get()
    widget = event.widget
    if n1.isdigit() and n2.isdigit:
        if widget == summa:
            result = str(float(n1) + float(n2))
        elif widget == sub:
            result = str(float(n1) - float(n2))
        elif widget == multiply:
            result = str(float(n1) * float(n2))
        elif widget == divide:
            if n2 == 0:
                result = "Ошибка"
            else:
                result = str(float(n1) / float(n2))
    else:
        result = "Ошибка"
    answer.config(text=str(result))

if __name__ == '__main__':
    root = Tk()
    first_number = Entry(width=11)
    second_number = Entry(width=11)
    summa = Button(text="+", width=20)
    summa.bind("<Button-1>", calculate)
    sub = Button(text="-", width=20)
    sub.bind("<Button-1>", calculate)
    multiply = Button(text="*", width=20)
    multiply.bind("<Button-1>", calculate)
    divide = Button(text="/", width=20)
    divide.bind("<Button-1>", calculate)
    answer = Label(width=12,height=4, fg="black", bg="white", font="Arial 14")

    first_number.pack()
    second_number.pack()
    summa.pack()
    sub.pack()
    multiply.pack()
    divide.pack()
    answer.pack()

    root.mainloop()
