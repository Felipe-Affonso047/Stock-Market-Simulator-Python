#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program has stocks

import random

company1_price = 10
company2_price = 5
company3_price = 50
company4_price = 40


def fluctuation():
    global company1_price
    global company2_price
    global company3_price
    global company4_price

    company1_price = company1_price + 1 + random.randint(-1000, 1000) / 100
    if company1_price <= 0:
        company1_price = company1_price - company1_price + random.randint(0, 9)
    company2_price = company2_price + 0.5 + random.randint(-100, 100) / 100
    if company2_price <= 0:
        company2_price = company2_price - company2_price + random.randint(0, 9)
    company3_price = company3_price - 0.1 + random.randint(-1000, 1000) / 10
    if company3_price <= 0:
        company3_price = company3_price - company3_price + random.randint(0, 9)
    company4_price = company4_price + random.randint(-1000, 1000) / 100
    if company4_price <= 0:
        company4_price = company4_price - company4_price + random.randint(0, 9)
    

def fluctuation_test():
    global company1_price
    global company2_price
    global company3_price
    global company4_price

    company1_price = company1_price + 1 + random.randint(-1000, 1000) / 100
    if company1_price <= 0:
        company1_price = company1_price - company1_price + random.randint(0, 9)
    company2_price = company2_price + 0.5 + random.randint(-100, 100) / 100
    if company2_price <= 0:
        company2_price = company2_price - company2_price + random.randint(0, 9)
    company3_price = company3_price - 0.1 + random.randint(-1000, 1000) / 10
    if company3_price <= 0:
        company3_price = company3_price - company3_price + random.randint(0, 9)
    company4_price = company4_price + random.randint(-1000, 1000) / 100
    if company4_price <= 0:
        company4_price = company4_price - company4_price + random.randint(0, 9)
    
    print("{0}, {1}, {2}, {3}".format(company1_price, company2_price, company3_price, company4_price))
    input()
    fluctuation_test()
