# Created by Nikolai Tiugaev for TumoLabs.
# Task 2. Craps game.
# The player should roll two dice. If the sum of both of them is 7 or 11 the player wins.
# If the sum is 2, 3 or 12 (craps) the casino wins.
# If during the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the “goal” number.
# To win, the player should roll the dice till they roll the goal number again.
# If the player rolls a 7 before rolling the goal number, they lose.


from random import randint
from time import sleep


# Introducing functions
def roll_dice() -> str:
    """
    Creating two random numbers as rolling dice
    :return: sum of created numbers as string
    """
    d1: int = randint(1, 6)
    d2: int = randint(1, 6)
    print(f'The sum of dice is {d1} + {d2} = {d1+d2}')
    return str(d1 + d2)


def targets_announce(tgt_win: tuple, tgt_lose: tuple) -> None:
    """
    Just printing the tuple of targets
    :param tgt_win:
    :param tgt_lose:
    :return: None
    """
    print(f'The goal to win is number(s): ', ', '.join(tgt_win))
    sleep(0.5)
    print(f'Your losing sum is number(s): ', ', '.join(tgt_lose))


def win_lose_bool(s_d: str, tgt_win: tuple, tgt_lose: tuple) -> bool:
    """
    Checking status of the game. If sum of dice win or lose than return True
    :param s_d:
    :param tgt_win:
    :param tgt_lose:
    :return: boolean
    """
    if s_d in tgt_win:
        print('Congratulations, you won! Good bye!')
        return True

    if s_d in tgt_lose:
        print('Oops, you lost! Good bye!')
        return True

    return False


# Starts main part
while True:
    print("Let's play the game!")
    target_win, target_lose = ('7', '11',), ('2', '3', '12',)     # initial values of targets
    sleep(0.5)
    targets_announce(target_win, target_lose)
    sleep(0.5)
    user_input: str = input('Please press enter to start the game or input q to quit: ')
    sleep(0.5)

    if user_input == 'q':
        print('Game interrupted. Good bye!')
        break

    if user_input not in ('q', None, ""):
        print('Incorrect input, try again.')
        continue

    sum_d: str = roll_dice()    # First rolling dice
    sleep(0.5)

    # if sum_d finds the winner then stop the game
    if win_lose_bool(sum_d, target_win, target_lose):
        break

    # when winner wasn't determined then initiating new targets to win and to lose
    target_win, target_lose = (str(sum_d),), ('7',)
    targets_announce(target_win, target_lose)
    sleep(0.5)

    # rolling dice till win or lose
    while True:
        sum_d = roll_dice()
        sleep(0.5)

        # if sum_d finds the winner then stop the game
        if win_lose_bool(sum_d, target_win, target_lose):
            break

    break
# end of main part
