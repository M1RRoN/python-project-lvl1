#!/usr/bin/env python3


import random
import prompt
from brain_games.scripts.brain_games import greet


def main():
    greet()
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string("You answer: ")
        if number % 2 == 0:
            if answer == "yes":
                print('Correct!')
            else:
                print(f"Let's try again, {name}!")
                break
        if number % 2 != 0:
            if answer == "yes":
                print(f"Let's try again, {name}!")
                break
            else:
                print('Correct!')
        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")
