#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def new_text(value):
    label.config(text=value)


if __name__ == "__main__":
    root = Tk()
    buttons = ["Вася", "Петя", "Маша"]
    numbers = ["88888888888", "+4 9087654321", "80000000000"]
    frame1 = Frame(root)
    frame1.pack(side=LEFT, padx=5, pady=5)
    for name, number in zip(buttons, numbers):
        Radiobutton(frame1, text=name, indicatoron=0, width=15, height=2,
                    command=lambda num=number: new_text(num)).pack(pady=2)
    frame2 = Frame(root, bg="white")
    frame2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
    label = Label(frame2, bg="white", width=30, anchor="center")
    label.pack(expand=True, fill=BOTH)
    root.mainloop()
