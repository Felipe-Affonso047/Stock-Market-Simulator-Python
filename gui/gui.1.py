#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program simulates the Stock Market

from tkinter import *

root = Tk()

r = StringVar()


def response():
    if_var = r.get()

    my_response1 = Label(root, text="Well that's good!", fg="green")
    my_response2 = Label(root, text="Well that's not good...", fg="red")

    if if_var == "good" or "well":
        my_response1.pack()
    elif if_var == "bad" or "not good":
        my_response2.pack()


how_are_you = Entry(root, textvariable=r)
my_label3 = Label(root, text="How are you?")
button = Button(root, text="send response.", command=response)

my_label3.pack()
how_are_you.pack()
button.pack()

root.mainloop()
