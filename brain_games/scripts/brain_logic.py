#!/usr/bin/env python3


import prompt
import random
import sympy


def greet():
    print("Welcome to the Brain Games!")


def brain_calc():
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, 20)
        expression = f"{num1} {random.choice('+-*')} {num2}"
        result = eval(expression)
        print(f'Question: {expression}')
        answer = prompt.string("You answer: ")
        if int(answer) == int(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")


def brain_even():
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string("You answer: ")
        if number % 2 == 0:
            if answer == "yes":
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        if number % 2 != 0:
            if answer == "yes":
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
            else:
                print('Correct!')
        i += 1
        if i == 3:
            print(f"Congratulations, {name}!")


def brain_gcd():
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


def brain_prime():
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


def brain_progression():
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