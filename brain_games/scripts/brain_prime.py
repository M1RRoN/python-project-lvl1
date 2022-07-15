#!/usr/bin/env python3

import sympy
import random
import prompt
from brain_games.scripts.brain_games import greet





def main():
    greet()
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string("You answer: ")
        
        if sympy.isprime(number):
            correct_answer = "yes"
            if answer == correct_answer:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                break
        else:
            correct_answer = "no"
            if answer == correct_answer:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                break

        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")

        
