import random


DESCRIPTION = 'What number is missing in the progression?'
NUM1_MIN, NUM1_MAX = 1, 10
NUM2_MIN, NUM2_MAX = 80, 100
N_MIN, N_MAX = 2, 10
RANDOM_INDEX_MIN, RANDOM_INDEX_MAX = 0, 4
SYMBOLS_COUNT = 5


def get_question_and_answer():
    num1 = random.randint(NUM1_MIN, NUM1_MAX)
    num2 = random.randint(NUM2_MIN, NUM2_MAX)
    n = random.randint(N_MIN, N_MAX)
    question, correct_answer = get_progression(num1, num2, n)
    return question, str(correct_answer)


def get_progression(num1, num2, n):
    numbers = []
    for j in range(num1, num2, n):
        numbers.append(j)
    numbers.sort()
    random_index = random.randint(RANDOM_INDEX_MIN, RANDOM_INDEX_MAX)
    correct_answer = numbers[random_index]
    numbers[random_index] = '..'
    progression_string = ' '.join(map(str, numbers[:SYMBOLS_COUNT]))
    return progression_string, correct_answer
