#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program has stocks

import random

company1_price = 10
company2_price = 5
company3_price = 50
company4_price = 40


def flutuation():
    global company1_price
    global company2_price
    global company3_price
    global company4_price

    company1_price = company1_price + 1 + random.randint(-1000, 1000) / 100
    company2_price = company2_price + 0.5 + random.randint(-100, 100) / 100
    company3_price = company3_price - 0.1 + random.randint(-1000, 1000) / 10
    company4_price = company4_price + random.randint(-1000, 1000) / 100
    

def flutuation_test():
    global company1_price
    global company2_price
    global company3_price
    global company4_price

    company1_price = company1_price + 1 + random.randint(-1000, 1000) / 100
    company2_price = company2_price + 0.5 + random.randint(-100, 100) / 100
    company3_price = company3_price - 0.1 + random.randint(-1000, 1000) / 10
    company4_price = company4_price + random.randint(-1000, 1000) / 100
    
    print("{0}, {1}, {2}, {3}".format(company1_price, company2_price, company3_price, company4_price))
    input()
    flutuation_test()


if __name__ == "__main__":
    flutuation_test()
