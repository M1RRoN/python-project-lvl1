#!/usr/bin/env python3


import random
import prompt
from brain_games.games.brain_logic import congratulations, greet
from brain_games.games.brain_logic import player_name, comparison


def brain_calc():
    greet()
    player_name()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        choice_of_sign = random.choice('+-*')
        expression = f"{num1} {choice_of_sign} {num2}"
        if choice_of_sign == "+":
            correct_answer = num1 + num2
        elif choice_of_sign == "-":
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        print(f'Question: {expression}')
        answer = prompt.string('You answer: ')
        if comparison(int(answer), int(correct_answer)) is False:
            break
        i += 1
        if i == 3:
            congratulations()
