#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program simulates the Stock Market

import math
import stock
import random

user_money = float(0)
user_shares = float(0)


def selling_stocks():
    global user_money
    global user_shares

    stock.flutuation()

    share = input("\nWich share do you want to sell?")

    if share == "company1":
        print("Share value: ${:,.2f}".format(stock.company1_price))
        number_of_shares_to_buy = int(input("How many shares do you want?"))
        price_of_bid = float(input("For how much each share?"))
        if price_of_bid >= stock.company1_price:
            user_money = user_money - (number_of_shares_to_buy * price_of_bid)
            user_shares = number_of_shares_to_buy + user_shares
            print("comfirmed transaction")
    else:
        print("This company does not exist.")
        buying_stocks()

    broker()


def buying_stocks():
    global user_money
    global user_shares

    stock.flutuation()

    share = input("\nWich share do you want to bid in?")

    if share == "company1":
        print("Share value: ${:,.2f}".format(stock.company1_price))
        number_of_shares_to_buy = int(input("How many shares do you want?"))
        price_of_bid = float(input("For how much each share?"))
        if price_of_bid >= stock.company1_price:
            user_money = user_money - (number_of_shares_to_buy * price_of_bid)
            user_shares = number_of_shares_to_buy + user_shares
            print("comfirmed transaction")
        else:
            print("transaction canceled")
    else:
        print("This company does not exist.")
        buying_stocks()

    broker()


def broker():
    global user_money
    global user_shares

    stock.flutuation()

    command = input("\nCommand for broker:")

    if command == "buy stocks":
        buying_stocks()
    elif command == "sell stocks":
        selling_stocks()
    elif command == "portifolio":
        main()
    elif command == "list stocks":
        print("company1: ${:,.2f}".format(stock.company1_price))
    elif command == "ls":
        print("buy stocks\nsell stocks\nlist stocks\nportifolio\nls")
    else:
        print("Invalid command")

    broker()


def withdraw():
    global user_money

    stock.flutuation()

    money_to_subtract = float(input(
        "\nHow much money do you want to withdraw from this account?"))

    user_money = user_money - money_to_subtract

    main()


def transfer():
    global user_money

    stock.flutuation()

    money_to_add = float(input(
        "\nHow much money do you want to transfer for this account?"))

    user_money = user_money + money_to_add

    main()


def main():
    global user_money
    global user_shares
    user_shares_value = 0
    total_user_money = 0
    command = 0

    stock.flutuation()

    user_shares_value = stock.company1_price * user_shares
    total_user_money = user_money + user_shares_value

    print("\nYour portifilio:")
    print("Money: ${:,.2f}".format(user_money))
    print("Shares:")
    print("Shares value: ${:,.2f}".format(user_shares_value))
    print("Total: ${:,.2f}".format(total_user_money))

    command = input("\nWaiting for command: ")

    if command == "broker":
        broker()
    elif command == "transfer":
        transfer()
    elif command == "withdraw":
        withdraw()
    elif command == "company1 price":
        print("company1: ${:,.2f}".format(stock.company1_price))
    elif command == "ls":
        print("broker\ntransfer\nwithdraw\ncompany1 price\nls")
    else:
        print("Invalid command")

    main()


if __name__ == "__main__":
    main()
