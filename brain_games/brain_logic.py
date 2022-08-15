import prompt


MESSAGE = 'is wrong answer ;(. Correct answer was'
NUMBER_OF_GAMES = 3


def welcome_name():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    return name


def player_answer():
    if correct_answer == 'yes' or 'no':
        answer = prompt.string('You answer: ')
    else:
        answer = prompt.string('You answer: ')
    return comparison(answer, correct_answer)


def play(game):
    welcome_name()
    print(game.DESCRIPTION)
    for i in range(NUMBER_OF_GAMES):
        global correct_answer
        correct_answer = game.get_question_and_answer()
        answer = player_answer()
        if answer is False:
            break
        if i == 2:
            congratulations()


def comparison(answer, correct_answer):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"{answer} {MESSAGE} '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


def congratulations():
    print(f'Congratulations, {name}!')
