#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

def open_file():
    file_name = entry.get()
    if file_name:
        with open(file_name, 'r', encoding="utf-8") as file:
            content = file.read()
            text.delete(1.0, END)
            text.insert(1.0, content)

def save_file():
    file_name = entry.get()
    if file_name:
        with open(file_name, 'w', encoding="utf-8") as file:
            content = text.get(1.0, END).strip()
            file.write(content)

if __name__ == "__main__":
    root = Tk()
    frame1 = Frame(root)
    frame1.pack()
    entry = Entry(frame1, width=60)
    entry.pack(side=LEFT)
    open_button = Button(frame1, width=10,
                         text="Открыть", command=open_file)
    open_button.pack(side=LEFT)
    save_button = Button(frame1, width=10,
                         text="Сохранить", command=save_file)
    save_button.pack(side=LEFT)
    frame2 = Frame(root)
    frame2.pack(fill=BOTH, expand=True)

    x_scroll = Scrollbar(frame2, orient=HORIZONTAL)
    x_scroll.pack(side=BOTTOM, fill=X)

    y_scroll = Scrollbar(frame2, orient=VERTICAL)
    y_scroll.pack(side=RIGHT, fill=Y)
    text = Text(frame2, wrap=NONE, width=60, height=20,
                xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
    text.pack(side=LEFT, fill=BOTH, expand=True)
    x_scroll.config(command=text.xview)
    y_scroll.config(command=text.yview)
    root.mainloop()

