"""Represents a player and tracks their name and scorecard."""

from scorecard import Scorecard

class Player:
    """Represents the player.

    Attributes:
        _name (str) = player's name
        _scorecard (Scorecard) = the player's scorecard
    """

    def __init__(self, name):
        """Take the player's name and create their scorecard.
        
        Parameters:
            name (str) = the player's name
        """
        self._name = name
        self._scorecard = Scorecard()

    @property
    def name(self) -> str:
        """Return player's name.
        
        Returns:
            _name (str)
        """
        return self._name

    @property
    def scorecard(self) -> Scorecard:
        """Return player's scorecard.
        
        Returns:
            _scorecard (Scorecard)
        """
        return self._scorecard

    def __str__(self):
        """Print player's name and their score.
        
        Returns:
            (str)
        """
        return ('Player: ' + self.name + f'\n{self.scorecard.grand_total}')