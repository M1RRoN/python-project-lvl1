import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def get_question_and_answer():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    return question, is_even(question)


def is_even(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
