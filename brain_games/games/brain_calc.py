import random


DESCRIPTION = 'What is the result of the expression?'
MIN = 0
MAX = 20


def get_question_and_answer():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    choice_of_sign = random.choice('+-*')
    expression = f'{num1} {choice_of_sign} {num2}'
    if choice_of_sign == '+':
        correct_answer = num1 + num2
    elif choice_of_sign == '-':
        correct_answer = num1 - num2
    elif choice_of_sign == '*':
        correct_answer = num1 * num2
    print(f'Question: {expression}')
    return str(correct_answer)
