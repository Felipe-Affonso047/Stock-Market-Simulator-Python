#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program simulates a Stock Market Broker

from tkinter import *
import time


def broker(inicial_cash):
    import stock

    stock.portfolio["cash"] = inicial_cash
    stock.portfolio["total"] = inicial_cash

    def buy_stocks():
        buy_stocks_scene = Toplevel()

        def buy_logic():
            try:
                company_name = stock_name.get()
                quantity_float = float(quantity.get())
                for company in range(len(stock.company_list)):
                    if stock.company_list[company]["name"] == company_name:
                        total_price = quantity_float * stock.company_list[company]["price"]
                        if stock.portfolio["cash"] >= total_price:
                            stock.portfolio["cash"] += - total_price
                            stock.company_list[company]["users"] += quantity_float
                buy_stocks_scene.destroy()
                broker_scene.destroy()
            except:
                error.pack()
    
        stock_name = StringVar()
        quantity = StringVar()

        stock_name_text = Label(buy_stocks_scene, text="Insert the name of the stock you want to buy (example: TSL4):")
        stock_name_inser = Entry(buy_stocks_scene, border=5, font=("", 20), textvariable=stock_name)
        quantity_text = Label(buy_stocks_scene, text="Insert the quantity of stocks you want to buy:")
        quantity_inser = Entry(buy_stocks_scene, border=5, font=("", 20), textvariable=quantity)
        buy_button_2 = Button(buy_stocks_scene, text="BUY", font=("", 20), command=buy_logic, background="#01C801")
        error = Label(text="ERROR\nTry again please.", font=("", 20), background="#FF0101")

        stock_name_text.pack()
        stock_name_inser.pack()
        quantity_text.pack()
        quantity_inser.pack()
        buy_button_2.pack()

        buy_stocks_scene.mainloop()
        return

    def sell_stocks():
        sell_stocks_scene = Toplevel()

        def sell_logic():
            try:
                company_name = stock_name.get()
                quantity_float = float(quantity.get())
                for company in range(len(stock.company_list)):
                    if stock.company_list[company]["name"] == company_name:
                        total_price = quantity_float * stock.company_list[company]["price"]
                        if stock.company_list[company]["users"] <= quantity_float:
                            stock.portfolio["cash"] += total_price
                            stock.company_list[company]["users"] += - quantity_float
                sell_stocks_scene.destroy()
                broker_scene.destroy()
            except:
                error.pack()
    
        stock_name = StringVar()
        quantity = StringVar()

        stock_name_text = Label(sell_stocks_scene, text="Insert the name of the stock you want to sell (example: TSL4):")
        stock_name_inser = Entry(sell_stocks_scene, border=5, font=("", 20), textvariable=stock_name)
        quantity_text = Label(sell_stocks_scene, text="Insert the quantity of stocks you want to sell:")
        quantity_inser = Entry(sell_stocks_scene, border=5, font=("", 20), textvariable=quantity)
        buy_button_2 = Button(sell_stocks_scene, text="SELL", font=("", 20), command=sell_logic, background="#960132")
        error = Label(text="ERROR\nTry again please.", font=("", 20), background="#FF0101")

        stock_name_text.pack()
        stock_name_inser.pack()
        quantity_text.pack()
        quantity_inser.pack()
        buy_button_2.pack()

        sell_stocks_scene.mainloop()

    broker_scene = Tk()

    boolean = []
    boolean.append(True)

    while boolean[0] == True:
        def exit():
            boolean[0] = False
        # save the company prices from before
        temp_companies = []
        for company in range(len(stock.company_list)):
            if len(temp_companies) != len(stock.company_list):
                temp_companies.append(stock.company_list[company]["price"])
            else:
                temp_companies[company] = stock.company_list[company]["price"]

        stock.fluctuation()

        stock.portfolio["total"] = stock.portfolio["cash"]
        for company in range(len(stock.company_list)):
            part_of_total = stock.company_list[company]["users"] * stock.company_list[company]["price"]
            stock.portfolio["total"] = stock.portfolio["total"] + part_of_total

        try:
            for widgets in broker_scene.winfo_children():
                widgets.destroy()
        except:
            broker_scene = Tk()

        total_text = "TOTAL: " + str(stock.portfolio["total"])
        cash_text = "CASH: " + str(stock.portfolio["cash"])

        total_label = Label(text=total_text)
        cash_label = Label(text=cash_text)
        buy_button = Button(text="BUY", height=3, background="#01C801", command=buy_stocks)
        sell_button = Button(text="SELL", height=3, background="#960132", command=sell_stocks)
        exit_button = Button(text="exit", command=exit)

        total_label.grid(row=0, column=1, columnspan=2)
        cash_label.grid(row=0, column=3, columnspan=2)
        buy_button.grid(row=1, column=0)
        sell_button.grid(row=2, column=0, rowspan=2)
        exit_button.grid(row=0, column=0)

        for company in range(len(stock.company_list)):
            # this loop deal with all the companies
            if temp_companies[company] < stock.company_list[company]["price"]:
                text_color = "#01FF01"
            else:
                text_color = "#FF0101"

            text = stock.company_list[company]["name"] + "\n" + str(stock.company_list[company]["price"])
            shares_text = "Shares: " + str(stock.company_list[company]["users"])
            shares_value = stock.company_list[company]["users"] * stock.company_list[company]["price"]
            shares_value_text = "Value: " + str(shares_value)

            company_text = Label(broker_scene, text=text, background="#000000", fg=text_color, font=("", 20), width=7)
            user_company_shares = Label(text=shares_text)
            user_company_value = Label(text=shares_value_text)

            column = company + 1
            company_text.grid(row=1, column=column)
            user_company_shares.grid(row=2, column=column)
            user_company_value.grid(row=3, column=column)

        for counter in range(10):
            try:
                broker_scene.update_idletasks()
                broker_scene.update()
            except:
                broker_scene = Tk()
            time.sleep(0.1)

    broker_scene.destroy()


def money_printer():
    money_printer_scene = Tk()

    answer = StringVar()

    def submit():
        #try:
            result = float(answer.get())
            money_printer_scene.destroy()
            return broker(result)
        #except Exception:
            #error = Label(text="ERROR\nTry entering a number.", font=("", 20), background="#FF0101")
            #error.grid()

    question = Label(text="How much money you want to start with?", font=("", 20), background="#01C801")
    response_box = Entry(border=5, font=("", 20), textvariable=answer)
    submit_num = Button(text="SUBMIT", width=20, font=("", 12), border=5, background="#960132", command=submit)

    question.grid(row=0, column=0, columnspan=2)
    response_box.grid(row=1, column=0)
    submit_num.grid(row=1, column=1)

    money_printer_scene.mainloop()

def start():
    def start_button_fun():
        start_scene.destroy()
        return

    start_scene = Tk()

    title = Label(text="Stock Market Simulator", width=30, height=4, font=("", 32), background="#C89601")
    start_button = Button(text="START", width=46, font=("", 20), border=5, background="#960132", command=start_button_fun)

    title.grid(row=0, column=0, columnspan=3)
    start_button.grid(row=1, column=1)

    start_scene.mainloop()
    return money_printer()

if __name__ == "__main__":
    start()
