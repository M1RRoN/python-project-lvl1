#!/usr/bin/env python3


import random
import prompt
from brain_games.games.brain_logic import congratulations, greet
from brain_games.games.brain_logic import player_name, comparison


def brain_progression():
    greet()
    player_name()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(80, 100)
        n = random.randint(2, 10)
        numbers = []
        for j in range(num1, num2, n):
            numbers.append(j)
        numbers.sort()
        random_index = random.randint(0, 4)
        correct_answer = numbers[random_index]
        numbers[random_index] = ".."
        string = " ".join(map(str, numbers[0:5]))
        print(f'Question: {string}')
        answer = prompt.string('You answer: ')
        if comparison(int(answer), int(correct_answer)) is False:
            break
        i += 1
        if i == 3:
            congratulations()
