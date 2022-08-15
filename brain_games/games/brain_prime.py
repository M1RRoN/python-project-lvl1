import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 2
MAX = 20


def get_question_and_answer():
    number = random.randint(MIN, MAX)
    print(f'Question: {number}')
    k = 0
    for j in range(2, number // 2 + 1):
        if number % j == 0:
            k += 1
        if k <= 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    return correct_answer
