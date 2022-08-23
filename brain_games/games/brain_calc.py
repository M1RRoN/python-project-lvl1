import random


DESCRIPTION = 'What is the result of the expression?'
MIN_NUM = 0
MAX_NUM = 20


def get_question_and_answer():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    choice_of_operator = random.choice('+-*')
    expression = f'{num1} {choice_of_operator} {num2}'
    if choice_of_operator == '+':
        correct_answer = num1 + num2
    elif choice_of_operator == '-':
        correct_answer = num1 - num2
    elif choice_of_operator == '*':
        correct_answer = num1 * num2
    question = f'Question: {expression}'
    return question, str(correct_answer)
