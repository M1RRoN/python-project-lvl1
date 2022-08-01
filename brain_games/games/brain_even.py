#!/usr/bin/env python3


import random
import prompt
from brain_games.games.brain_logic import congratulations, greet, player_name, comparison


def brain_even():
    greet()
    player_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
            if comparison(answer, correct_answer) is False:
                break
        else:
            correct_answer = 'no'
            if comparison(answer, correct_answer) is False:
                break
        i += 1
        if i == 3:
            congratulations()
