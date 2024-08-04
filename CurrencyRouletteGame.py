import requests
from currency_converter import CurrencyConverter
import random


def get_money_interval(difficulty, t):
    c = CurrencyConverter()
    rate = c.convert(t, 'USD', 'ILS')
    interval = (rate - (5 - difficulty), rate + (5 - difficulty))
    return interval
def generate_number():
    return random.randint(1, 100)

def get_guess_from_user(t):
    while True:
        try:
            guess = float(input(f"Enter your guess for how much is {t}$ in ILS: "))
            break
        except BaseException as e:
            print("Please enter numerical guess")
            continue
    return guess

#get_money_interval(5, 10)

def play(difficulty):
    t = generate_number()
    guess = get_guess_from_user(t)
    interval = get_money_interval(difficulty, t)
    return True if interval[0] <= guess <= interval[1] else False
