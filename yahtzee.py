"""This module creates a Yahtzee game."""

from typing import List
from round import Round
from player import Player
from print_utils import clear_screen, print_logo, print_winner


class Yahtzee:
    """Class to initiate a game of Yahtzee.
    
    Attributes:
        _players ([Player]) = list of Players - number specified by user
                              upon initializing game
        _rounds ([Round]) = list of Rounds - number set by global NUM_ROUNDS
        NUM_ROUNDS (int) = number of rounds to be played. Standard game of Yahtzee
                           has 13 rounds.
    """

    NUM_ROUNDS = 13

    def __init__(self):
        """Set up a game of Yahtzee.

        Clears the terminal screen and displays the logo
        before having the user specify the number of players and create those players,
        and then finally it sets up the appropriate number of rounds to be played.
        """
        clear_screen()
        print_logo()
        self._players = self.create_players()
        self._rounds = self.create_rounds()

    @property
    def players(self):
        """Return list of Players.
        
        Returns:
            _players (List[Players])
        """
        return self._players

    @property
    def rounds(self):
        """Return list of Rounds.
        
        Returns:
            _rounds (List[Round])
        """
        return self._rounds

    def create_players(self):
        """Create List of Players.

        Will ask user how many Players there will be
        and then prompt user for their names

        Returns:
            players (List[Player]): the list of initialized Players
        """
        players = []
        try:
            num_players = int(input("  How many players? "))
        except:
            print("  Invalid number of players. Please enter again.")
            num_players = int(input("  How many players? "))

        for player in range(num_players):
            player_name = input(f"\n  What is player {player + 1}'s name? ")
            players.append(Player(player_name))

        return players

    def create_rounds(self):
        """Create List of Rounds according to the global NUM_ROUNDS.
        
        A standard game of Yahtzee
        has 13 rounds.

        Returns:
            (List[Round]): the list of initialized rounds
        """
        return [Round(self.players, round_num + 1)
                for round_num in range(self.NUM_ROUNDS)]

    def display_winner(self):
        """Display the winner in the case of a multiplayer game."""
        winner = max([player for player in self.players])
        print_winner(winner)



def main():
    """Initialize game and start game loop."""
    y = Yahtzee()

    for round in y.rounds:
        round.play_round()

    clear_screen()
    y.display_winner()


if __name__ == "__main__":
    main()
