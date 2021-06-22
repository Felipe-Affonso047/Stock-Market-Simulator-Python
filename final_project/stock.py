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

event1 = {
    "event_text": "This company just found the cure for cancer!!!!!!", "value_change": 1, "new_trend": 0.5
}
event2 = {
    "event_text": "This company main hub just got on fire!!!!!!", "value_change": -0.5, "new_trend": 0
}
event3 = {
    "event_text": "This company just won an award for best company!!!!!!", "value_change": 3, "new_trend": -0.5
}
event4 = {
    "event_text": "The CEO of the company, Steve Bojs, just died!!!!!!", "value_change": -0.7, "new_trend": 1
}

event_list = [event1] + [event2] + [event3] + [event4]

def decimal_rounding(numbers, decimals):
    # this function rounds decimals
    rounding_float = float((numbers * pow(10, decimals)) + 0.5)
    rounding_int = int(rounding_float)
    rounded_number = rounding_int / pow(10, decimals)
    return rounded_number


def fluctuation():
    for company in range(len(company_list)):
        company_list[company]["price"] += company_list[company]["trend"] + random.randint(-(company_list[company]["fr"]), company_list[company]["fr"]) / 100
        if company_list[company]["price"] <= 0:
            company_list[company]["price"] += random.randint(0, 9) - company_list[company]["price"]
        company_list[company]["price"] = decimal_rounding(company_list[company]["price"], 2)


def event():
    chance = random.randint(1, 50)
    if chance == 1:
        random_event = random.randint(0, len(event_list) - 1)
        random_company = random.randint(0, len(company_list) - 1)
        before_decimal = company_list[random_company]["price"] + company_list[random_company]["price"] * event_list[random_event]["value_change"]
        company_list[random_company]["trend"] =+ event_list[random_event]["new_trend"]
        company_list[random_company]["price"] = decimal_rounding(before_decimal, 2)
        return_list = ["true"] + [company_list[random_company]["name"]] + [event_list[random_event]["event_text"]]
        return return_list
    else:
        return_list = ["false"]
        return return_list
