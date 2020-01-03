import time
import random
import sys
from time import sleep


money = 100

# Loading


def loading():
    loading = '='*15
    print('Flipping the coin...')
    for i in loading:
        print(i),
        sys.stdout.flush()
        sleep(0.1)
    print('\n'*2)


def coin_flip(bet, choice):
    # Generate random num
    random.seed(time.clock())
    num = random.randint(1, 2)

    # Text outputs
    hline = '-'*20
    invalid_bet = hline + '\n' + 'Your bet should be above 0.' + '\n' + hline
    heads_text = 'Coin lands on Heads!' + '\n' + hline + '\n'
    tails_text = 'Coin lands on Tails!' + '\n' + hline + '\n'
    choice_text = '\n'*2 + hline + '\n' + \
        'Your choice is ' + choice + '\n' + hline + '\n'*2
    won_text = 'You won!' + '\n'*2 + hline
    lost_text = 'You lost!' + '\n'*2 + hline

    # Test if bet was above 0
    if bet <= 0:
        print(invalid_bet)
        return 0

    # Announce player's choice
    print(choice_text)

    # Display loading animation
    loading()

    # Announce the face coin landed on
    if num == 1:
        print(heads_text)
    else:
        print(tails_text)

    # Announce if player wins / looses and adjust total money
    if (choice == 'heads' and num == 1) or (choice == 'tails' and num == 2):
        print(won_text)
        return bet
    else:
        print(lost_text)
        return -bet


# Call function here
money += coin_flip(20, 'heads')
