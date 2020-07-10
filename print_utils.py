"""Utilities to assist in printing different items to the terminal."""
from os import system, name

def clear_screen():
    """Clear the terminal."""
    # for windows
    if name == "nt":
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def print_dice_row(dice):
    """Print dice out in a row.
    
    Parameters:
        dice (Dice) = dice to print out
    """
    top_row = " .---------. " * 5 + "\n"
    bottom_row = " '---------' " * 5 + "\n"
    one_rows = [" |         | ", " |    O    | ", " |         | "]
    two_rows = [" |  O      | ", " |         | ", " |      O  | "]
    three_rows = [" |  O      | ", " |    O    | ", " |      O  | "]
    four_rows = [" |  O   O  | ", " |         | ", " |  O   O  | "]
    five_rows = [" |  O   O  | ", " |    O    | ", " |  O   O  | "]
    six_rows = [" |  O   O  | ", " |  O   O  | ", " |  O   O  | "]
    dice_rows = [one_rows, two_rows, three_rows, four_rows, five_rows, six_rows]
    second_row = ""
    third_row = ""
    fourth_row = ""

    dice_numbers = ""
    for x in range(1, 6):
        dice_numbers += str(x).center(13)

    for die in dice:
        second_row += dice_rows[die.value - 1][0]
        third_row += dice_rows[die.value - 1][1]
        fourth_row += dice_rows[die.value - 1][2]

    print("\n " + dice_numbers + "\n " + top_row + " " + second_row + "\n " + third_row + "\n " + fourth_row + "\n " + bottom_row)


def print_logo():
    """Print the Yahtzee Logo."""
    print("\n\n")
    for row in logo:
        print(" " * 20 + row, end='')
    print("\n\n")


def print_scorecard(round_num, player):
    """Print the player's scorecard.
    
    Parameters:
        round_num (int) = round number
        player (Player) = the player whose scorecard is being displayed
    """
    print(f"\n  Round #{round_num}")
    print(f"\n  Player {player.name}\n")
    print(player.scorecard)
    print()

def print_winner(player):
    """Print a message to the winner.

    Parameters:
        player (Player)
    """
    print(f"\n  Congratulations to {player.name}!\n  Your final score was {player.scorecard.grand_total}.")


logo = [" .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. .----------------.\n", 
        "| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |\n",
        "| |  ____  ____  | | |      __      | | |  ____  ____  | | |  _________   | | |   ________   | | |  _________   | | |  _________   | |\n",
        "| | |_  _||_  _| | | |     /  \     | | | |_   ||   _| | | | |  _   _  |  | | |  |  __   _|  | | | |_   ___  |  | | | |_   ___  |  | |\n",
        "| |   \ \  / /   | | |    / /\ \    | | |   | |__| |   | | | |_/ | | \_|  | | |  |_/  / /    | | |   | |_  \_|  | | |   | |_  \_|  | |\n",
        "| |    \ \/ /    | | |   / ____ \   | | |   |  __  |   | | |     | |      | | |     .'.' _   | | |   |  _|  _   | | |   |  _|  _   | |\n",
        "| |    _|  |_    | | | _/ /    \ \_ | | |  _| |  | |_  | | |    _| |_     | | |   _/ /__/ |  | | |  _| |___/ |  | | |  _| |___/ |  | |\n",
        "| |   |______|   | | ||____|  |____|| | | |____||____| | | |   |_____|    | | |  |________|  | | | |_________|  | | | |_________|  | |\n",
        "| |              | | |              | | |              | | |              | | |              | | |              | | |              | |\n",
        "| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |\n",
        " '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------'"]