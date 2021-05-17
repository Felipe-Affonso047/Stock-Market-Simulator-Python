#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program says Hello

from tkinter import *

root = Tk()

name = StringVar()


def response():
    hello = "Hello " + name.get()
    my_response = Label(root, text=hello)

    if str(my_response) == "hi":
        my = Label(root, text="OMG")
        my.pack()

    my_response.pack()


my_label = Label(root, text="What is your name?")
my_entry = Entry(root, textvariable=name)
my_button = Button(root, text="submit", command=response)

my_label.pack()
my_entry.pack()
my_button.pack()


root.mainloop()
