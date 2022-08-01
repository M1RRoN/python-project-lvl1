#!/usr/bin/env python3


import prompt


message = 'is wrong answer ;(. Correct answer was'


def greet():
    print('Welcome to the Brain Games!')


def player_name():
    global name
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')


def comparison(answer, correct_answer):
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"{answer} {message} '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def congratulations():
    print(f'Congratulations, {name}!')
