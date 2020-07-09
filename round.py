"""Round of playing Yahtzee. Includes taking turns and scoring."""

from dice import Dice
from die import Die

class Round:
    """Class to create Round in a game of Yahtzee.

    Attributes:
        _players ([Player]) = list of Players
        _round_num (int) = which round number this represents
    """

    # Number of times the dice can be rolled per turn
    NUM_TURNS = 3
    DICE = Dice(dice=[Die("1", 6), Die("2", 6),
                      Die("3", 6), Die("4", 6),
                      Die("5", 6)])

    def __init__(self, players: List(Player), round_num: int):
        """Set up a round.

        Parameters:
            players (List[Player]) = list of players
            round_num (int) = which round number this represents
        """
        self._players = players
        self._round_num = round_num

    def play_round(self):
        """Play a round for each player."""
        clear_screen()

        for player in self.players:
            self.take_turns(player)
            if len(self.players) > 1:
                input(f"\n  Press <ENTER> to start next player's turn")

    def take_turns(self, player: Player):
        """Take a turn - rolling dice up to 3 times.

        During a turn, the dice are rolled and the player
        is able to select dice to keep.
        
        Parameters:
            Player = the player taking the turn
        """
        turn_num = 1
        keep_rolling = True

        print_scorecard(self.round_num, player)

        self.DICE.roll()
        while turn_num <= 2 and keep_rolling is True:
            clear_screen()
            print_scorecard(self.round_num, player)
            print_dice_row(self.DICE)

            kept_dice = input("\n\n  Which dice would you like to keep? ")
            keep_rolling = self.parse_kept_dice(kept_dice, keep_rolling)

            turn_num += 1
        
        clear_screen()
        print_scorecard(self.round_num, player)
        print_dice_row(self.DICE)
        self.score_round(player)

    def parse_kept_dice(self, kept_dice, keep_rolling) -> bool:
        """Determine which dice the player wants to keep.

        Parameters:
            kept_dice (str) = input str from the player
            keep_rolling (bool) = whether to continue rolling

        Returns:
            keep_rolling (bool) = whether to continue rolling
        """
        # Player pressed enter and isn't keeping any dice
        if (len(kept_dice) == 0):
            self.DICE.roll()
            keep_rolling = True
        
        # Player is keeping some/all dice
        else:
            # Player is keeping all dice
            # and ending turn
            kept_dice = kept_dice.split()
            if (len(kept_dice) == 5):
                keep_rolling = False
            
            # Player is keeping some dice
            else:
                kept_dice = [(int(index) - 1) for index in kept_dice]

                # roll the dice not being kept
                for x in range(len(self.DICE)):
                    if (x not in kept_dice):
                        self.DICE[x].roll()
                keep_rolling = True
        return keep_rolling
                
    def score_round(self, player):
        """Score the category indicated by the player.

        Parameters:
            player (Player) = the player scoring
        """
        selection = input("\n\n  Which category would you like to score? ")
        player.scorecard.score(selection, self.DICE)
        clear_screen()
        print_scorecard(self.round_num, player)

    @property
    def round_num(self) -> int:
        """Which number round this instance is in the whole game.
        
        Returns:
            _round_num (int)
        """
        return self._round_num

    @property
    def players(self) -> [Player]:
        """List of Players in the round.
        
        Returns:
            _players (List[Player])
        """
        return self._players
