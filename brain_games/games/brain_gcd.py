import random
import math

from brain_games.games.brain_even import MIN_NUMBER


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 100


def get_question_and_answer():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'Question: {num1} {num2}'
    correct_answer = math.gcd(num1, num2)
    return question, str(correct_answer)
