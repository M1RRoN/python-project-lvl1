#!/usr/bin/env python3


import random
import prompt
from brain_games.scripts.brain_games import greet


def main():
    greet()
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        expression = f"{num1} {random.choice('+-*')} {num2}"
        result = eval(expression)
        print(f'Question: {expression}')
        answer = prompt.string("You answer: ")
        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")
