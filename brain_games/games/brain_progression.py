import random


DESCRIPTION = 'What number is missing in the progression?'
NUM1_MIN, NUM1_MAX = 1, 10
NUM2_MIN, NUM2_MAX = 80, 100
N_MIN, N_MAX = 2, 10


def get_question_and_answer():
    num1 = random.randint(NUM1_MIN, NUM1_MAX)
    num2 = random.randint(NUM2_MIN, NUM2_MAX)
    n = random.randint(N_MIN, N_MAX)
    numbers = []
    for j in range(num1, num2, n):
        numbers.append(j)
    numbers.sort()
    random_index = random.randint(0, 4)
    correct_answer = numbers[random_index]
    numbers[random_index] = '..'
    string = ' '.join(map(str, numbers[0:5]))
    print(f'Question: {string}')
    return str(correct_answer)
