import random

items = {1: 'rock', 2: 'paper', 3: 'scissors'}


def select_winner(user_choice):
    if user_choice not in ('1', '2', '3'):
        return print('Make correct choice!')
    computer_choice = random.randrange(1, 3, 1)
    print('Computer choice: ', items[computer_choice])
    who_win = (int(user_choice) - computer_choice) % 3
    if who_win == 0:
        print('draw')
    elif who_win == 1:
        print('You won!')
    else:
        print('You lost')


while True:
    select_winner(input('Make your choice (1 - rock, 2 - paper, 3 - scissors): '))
    if input('Want you more? Y, y or N, n: ') in ('Y', 'y'):
        continue
    else:
        break
print('Bye!')
