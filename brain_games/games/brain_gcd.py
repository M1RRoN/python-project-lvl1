import random
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN = 1
MAX = 100


def get_question_and_answer():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    print(f'Question: {num1} {num2}')
    correct_answer = math.gcd(num1, num2)
    return str(correct_answer)
