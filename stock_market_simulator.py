#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program simulates the Stock Market

import math

user_money = float(0)
user_shares = float(0)

def broker():
    global user_money
    global user_shares

    share = input("\nWich share do you want to bid in?")
    number_of_shares_to_buy = int(input("How many shares do you want?"))
    price_of_bid = float(input("For how much each share?"))
    user_money = user_money - (number_of_shares_to_buy * price_of_bid)
    user_shares = number_of_shares_to_buy + user_shares
    
    main()


def add_money():
    global user_money

    money_to_add = float(input("\nHow much money do you want to add?"))

    user_money = user_money + money_to_add
    
    main()

def main():
    global user_money
    global user_shares
    command = 0
    
    print("\nYour portifilio:")
    print("Money: ${:,.2f}".format(user_money))
    print("Shares: {}".format(user_shares))

    command = input("\nWaiting for command: ")

    if command == "buy shares":
        broker()

    if command == "add money":
        add_money()


if __name__ == "__main__":
    main()
