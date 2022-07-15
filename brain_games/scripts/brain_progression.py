#!/usr/bin/env python3


import random
import prompt
from brain_games.scripts.brain_games import greet


def main():
    greet()
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
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
        random_index = random.randint(0, 9)
        correct_answer = numbers[random_index]
        numbers[random_index] = ".."
        string = " ".join(map(str, numbers[0:10]))
        print(f'Question: {string}')
        answer = prompt.string("You answer: ")
        if int(answer) == int(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")
