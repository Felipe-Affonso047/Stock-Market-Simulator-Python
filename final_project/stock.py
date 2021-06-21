#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program has stocks

import random

portfolio = {
    "cash": 0, "total": 0
}

company1 = {
    "price": 10, "name": "TSL4", "trend": 0.5, "fr": 1000, "users": 0
}
company2 = {
    "price": 5, "name": "P3TR", "trend": 0.25, "fr": 100, "users": 0
}
company3 = {
    "price": 50, "name": "BK00", "trend": -0.1, "fr": 100, "users": 0
}
company4 = {
    "price": 40, "name": "B4NC", "trend": 0, "fr": 10, "users": 0
}

company_list = [company1] + [company2] + [company3] + [company4]


def decimal_rounding(numbers, decimals):
    # this function rounds decimals
    rounding_float = float((numbers * pow(10, decimals)) + 0.5)
    rounding_int = int(rounding_float)
    rounded_number = rounding_int / pow(10, decimals)
    return rounded_number


def weird_decimal_rounding(numbers, decimals):
    # this function rounds decimals
    rounding_float = float((numbers * pow(10, decimals)) + 0.9999)
    rounding_int = int(rounding_float)
    rounded_number = rounding_int / pow(10, decimals)
    return rounded_number


def fluctuation():
    global company_list

    for company in range(len(company_list)):
        company_list[company]["price"] += company_list[company]["trend"] + random.randint(-(company_list[company]["fr"]), company_list[company]["fr"]) / 100
        if company_list[company]["price"] <= 0:
            company_list[company]["price"] += random.randint(0, 9) - company_list[company]["price"]
        company_list[company]["price"] = decimal_rounding(company_list[company]["price"], 2)
