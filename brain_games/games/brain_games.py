import prompt


def player_greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
