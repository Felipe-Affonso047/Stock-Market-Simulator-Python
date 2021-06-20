#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program simulates a Stock Market Broker

from tkinter import *


def money_printer():
    money_printer_scene = Tk()

    answer = StringVar()

    def submit():
        try:
            result = float(answer.get())
        except Exception:
            error = Label(text="ERROR\nTry entering a number.", font=("", 20), background="#FF0101")
            error.grid()

    question = Label(text="How much money you want to start with?", font=("", 20), background="#01C801")
    response_box = Entry(text="ENTER A NUMBER", border=5, font=("", 20), textvariable=answer)
    submit_num = Button(text="SUBMIT", width=20, font=("", 12), border=5, background="#960132", command=submit)

    question.grid(row=0, column=0, columnspan=2)
    response_box.grid(row=1, column=0)
    submit_num.grid(row=1, column=1)

    money_printer_scene.mainloop()


def start():
    def start_button_fun():
        start_scene.destroy()
        money_printer()
        return

    start_scene = Tk()

    title = Label(text="Stock Market Simulator", width=30, height=4, font=("", 32), background="#C89601")
    start_button = Button(text="START", width=46, font=("", 20), border=5, background="#960132", command=start_button_fun)

    title.grid(row=0, column=0, columnspan=3)
    start_button.grid(row=1, column=1)

    start_scene.mainloop()


if __name__ == "__main__":
    start()
