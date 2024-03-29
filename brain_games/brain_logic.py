import prompt


GAMES_COUNT = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for i in range(1, GAMES_COUNT + 1):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        if correct_answer == 'yes' or 'no':
            answer = prompt.string('You answer: ')
        else:
            answer = prompt.string('You answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            wrong_answer = 'is wrong answer ;(. Correct answer was'
            print(f'{answer} {wrong_answer} \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            break
        if i == GAMES_COUNT:
            print(f'Congratulations, {name}!')
