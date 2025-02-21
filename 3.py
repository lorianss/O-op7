#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

def color(color_name, color_code):
    answer.config(text=color_name)
    entry.delete(0, 'end')
    entry.insert(0, color_code)

if __name__ == '__main__':
    root = Tk()
    button_widths = 3
    entry = Entry(root, justify="center")
    answer = Label(root)
    red = Button(root, width=button_widths, bg='#ff0000', command=lambda: color("Красный", "#ff0000"))
    orange = Button(root, width=button_widths, bg='#ff7d00', command=lambda: color("Оранжевый", "#ff7d00"))
    yellow = Button(root, width=button_widths, bg='#ffff00', command=lambda: color("Желтый", "#ffff00"))
    green = Button(root, width=button_widths, bg='#00ff00', command=lambda: color("Зеленый", "#00ff00"))
    light_blue = Button(root, width=button_widths, bg='#007dff', command=lambda: color("Голубой", "#007dff"))
    blue = Button(root, width=button_widths, bg='#0000ff', command=lambda: color("Синий", "#0000ff"))
    purple = Button(root, width=button_widths, bg='#7d00ff', command=lambda: color("Фиолетовый", "#7d00ff"))

    answer.pack()
    entry.pack()

    button_frame = Frame(root)
    button_frame.pack()
    red.pack(side=LEFT, padx=1)
    orange.pack(side=LEFT, padx=1)
    yellow.pack(side=LEFT, padx=1)
    green.pack(side=LEFT, padx=1)
    light_blue.pack(side=LEFT, padx=1)
    blue.pack(side=LEFT, padx=1)
    purple.pack(side=LEFT, padx=1)

    root.mainloop()
