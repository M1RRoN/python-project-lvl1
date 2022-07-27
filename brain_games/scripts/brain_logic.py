#!/usr/bin/env python3


import prompt
import random
import math


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


def brain_calc():
    player_name()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        expression = f"{num1} {random.choice('+-*')} {num2}"
        correct_answer = eval(expression)
        print(f'Question: {expression}')
        answer = prompt.string('You answer: ')
        if comparison(int(answer), int(correct_answer)) is False:
            break
        i += 1
        if i == 3:
            print(f'Congratulations, {name}!')


def brain_even():
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
            print(f'Congratulations, {name}!')


def brain_gcd():
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
            print(f"Congratulations, {name}!")


def brain_prime():  # noqa: C901
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
            print(f'Congratulations, {name}!')


def brain_progression():
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
            print(f'Congratulations, {name}!')
