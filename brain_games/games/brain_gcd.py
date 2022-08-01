#!/usr/bin/env python3


import random
import math
import prompt
from brain_games.games.brain_logic import congratulations, greet, player_name, comparison


def brain_gcd():
    greet()
    player_name()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('You answer: ')
        if comparison(int(answer), math.gcd(num1, num2)) is False:
            break
        i += 1
        if i == 3:
            congratulations()
