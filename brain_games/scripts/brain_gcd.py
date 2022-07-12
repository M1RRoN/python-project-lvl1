#!/usr/bin/env python3


import random
import prompt
from brain_games.scripts.brain_games import greet


def main():
    greet()
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        print(f'Question: {num1} {num2}')
        answer = prompt.string("You answer: ")
        if int(answer) == gcd(num1, num2):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd(num1, num2)}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1        
    return(num1)