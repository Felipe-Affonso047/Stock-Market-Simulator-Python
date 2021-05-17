#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program simulates the Stock Market

from tkinter import *

root = Tk()

how_are_you = Entry(root)


def response():

    if response1 == "good" or "well":
        my_response1 = Label(root, text="Well that's good!", fg="green")
        my_response1.pack()
    elif response1 == "bad" or "not good":
        my_response2 = Label(root, text="Well that's not good...", fg="red")
        my_response2.pack()

    root.mainloop()


def click():
    global how_are_you

    my_label3 = Label(root, text="How are you?")
    button = Button(root, text="send response.", command=response)

    my_label3.pack()
    how_are_you.pack()
    button.pack()

    root.mainloop()


def main():
    # creating a Label Widget (the windows were the GUI will be)
    my_button = Button(root, text="Click me", padx=10, pady=10, command=click)

    my_label1 = Label(root, text="Hello, World!", bg="black", fg="white")
    my_label2 = Label(root, text="My name is Felipe", borderwidth=10)

    # Putting it in the screen

    my_label1.pack()
    my_label2.pack()

    my_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
