#!/usr/bin/env python3


import random
import prompt
from brain_games.games.brain_logic import congratulations, greet
from brain_games.games.brain_logic import player_name, comparison


def brain_prime():  # noqa: C901
    greet()
    player_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ')
        k = 0
        for j in range(2, number // 2 + 1):
            if number % j == 0:
                k += 1
        if k <= 0:
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
