import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
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
    return str(correct_answer)
