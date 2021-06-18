#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program simulates a Stock Market Broker

from tkinter import *

root = Tk()


def main():
    title = Label(text="Stock Market Simulator", border=1, borderwidth=3, background="#7c0a02")

    title.grid(row=0, column=0, columnspan=3)

    root.mainloop()


if __name__ == "__main__":
    main()