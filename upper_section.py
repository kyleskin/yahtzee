"""Represents the upper section of the Yahtzee scorecard.

Includes aces, twos, threes, fours, fives, sixes, and the upper bonus.
"""

import errors

class UpperSection:
    """Represents the upper section of the Yahtzee scorecard.
    
    Attributes:
        _aces (int) = score for aces
        _aces_scored (bool) = if aces has been scored yet
        _twos (int) = score for twos
        _twos_scored (bool) = if twos has been scored yet
        _threes (int) = score for threes
        _threes_scored (bool) = if threes has been scored yet
        _fours (int) = score for fours
        _fours_scored (bool) = if fours has been scored yet
        _fives (int) = score for fives
        _fives_scored (bool) = if fives has been scored yet
        _sixes (int) = score for sixes
        _sixes_scored (bool) = if sixes has been scored yet
        _subtotal (int) = total without bonus
        _bonus (int) = score for bonus
        _bonus_earned (bool) = if the bonus has been earned yet
        _total (int) = total score for the upper section
    """

    def __init__(self):
        """Set up upper section of scorecard - all values zeroed out."""
        self._aces = 0
        self._aces_scored = False
        self._twos = 0
        self._twos_scored = False
        self._threes = 0
        self._threes_scored = False
        self._fours = 0
        self._fours_scored = False
        self._fives = 0
        self._fives_scored = False
        self._sixes = 0
        self._sixes_scored = False
        self._subtotal = 0
        self._bonus = 0
        self._bonus_earned = False
        self._total = 0

    @property
    def aces(self):
        """Get score for aces.
        
        Returns:
            self._aces (int)
        """
        return self._aces

    @aces.setter
    def aces(self, dice):
        """Score aces.

        Parameters:
            dice (Dice): the dice to be scored
        """
        if self.aces_scored:
            raise errors.AlreadyScored
        else:
            self._aces = sum(die.value for die in dice if die.value == 1) 
            self.aces_scored = True

    @property
    def aces_scored(self):
        """Determine if aces has been scored.
        
        Returns:
            _aces_scored (bool)
        """
        return self._aces_scored

    @aces_scored.setter
    def aces_scored(self, scored):
        """Set if aces has been scored.

        Parameters:
            scored (bool): whether the category has been scored
        """
        self._aces_scored = scored

    @property
    def twos(self):
        """Get score for twos.

        Returns:
            _twos (int)
        """
        return self._twos

    @twos.setter
    def twos(self, dice):
        """Score for twos.

        Parameters:
            dice (Dice): dice to be scored
        """
        if self.twos_scored:
            raise errors.AlreadyScored
        else:
            self._twos = sum(die.value for die in dice if die.value == 2) 
            self.twos_scored = True

    @property
    def twos_scored(self):
        """Determine if twos has been scored already.
        
        Returns:
            _twos_scored (bool)
        """
        return self._twos_scored

    @twos_scored.setter
    def twos_scored(self, scored):
        """Set if twos has been scored already.

        Parameters:
            scored (bool): whether the category has been scored
        """
        self._twos_scored = scored

    @property
    def threes(self):
        """Get score for threes.

        Returns:
            _threes (int)
        """
        return self._threes

    @threes.setter
    def threes(self, dice):
        """Score for threes.

        Parameters:
            dice (Dice): dice to be scored
        """
        if self.threes_scored:
            raise errors.AlreadyScored
        else:
            self._threes = sum(die.value for die in dice if die.value == 3)
            self.threes_scored = True

    @property
    def threes_scored(self):
        """Determine if threes has been scored already.

        Returns:
            _threes_scored (bool)
        """
        return self._threes_scored

    @threes_scored.setter
    def threes_scored(self, scored):
        """Set if threes has been scored.

        Parameters:
            scored: whether the category has been scored
        """
        self._threes_scored = scored

    @property
    def fours(self):
        """Get score for fours.

        Returns:
            _fours (int)
        """
        return self._fours

    @fours.setter
    def fours(self, dice):
        """Score fours.

        Parameters:
            dice (Dice): dice to be scored
        """
        if self.fours_scored:
            raise errors.AlreadyScored
        else:
            self._fours = sum(die.value for die in dice if die.value == 4)
            self.fours_scored = True

    @property
    def fours_scored(self):
        """Determine if fours has been scored already.

        Returns:
            _four_scored (bool)
        """
        return self._fours_scored

    @fours_scored.setter
    def fours_scored(self, scored):
        """Set if fours has been scored.

        Parameters:
            scored (bool): whether the category has been scored
        """
        self._fours_scored = scored

    @property
    def fives(self):
        """Score for fives.

        Returns:
            _fives (int)
        """
        return self._fives

    @fives.setter
    def fives(self, dice):
        """Score fives.

        Parameters:
            dice (Dice): dice to be scored
        """
        if self.fives_scored:
            raise errors.AlreadyScored
        else:
            self._fives = sum(die.value for die in dice if die.value == 5)
            self.fives_scored = True

    @property
    def fives_scored(self):
        """Determine if fives has been scored already.

        Returns:
            _fives_scored (bool)
        """
        return self._fives_scored

    @fives_scored.setter
    def fives_scored(self, scored):
        """Set if fives has been scored.

        Parameters:
            scored (bool): whether the category has been scored
        """
        self._fives_scored = scored

    @property
    def sixes(self):
        """Score for sixes.

        Returns:
            _sixes (int)
        """
        return self._sixes

    @sixes.setter
    def sixes(self, dice):
        """Score sixes.

        Parameters:
            dice (Dice): dice to be scored
        """
        if self.sixes_scored:
            raise errors.AlreadyScored
        else:
            self._sixes = sum(die.value for die in dice if die.value == 6)
            self.sixes_scored = True

    @property
    def sixes_scored(self):
        """Determine if sixes has been scored already.

        Returns:
            _sixes_scored (bool)
        """
        return self._sixes_scored

    @sixes_scored.setter
    def sixes_scored(self, scored):
        """Set if sixes has been scored.

        Parameters:
            _sixes_scored (bool): whether the category has been scored
        """
        self._sixes_scored = scored

    @property
    def subtotal(self):
        """Subtotal of categories before bonus.

        Returns:
            subtotal (int)
        """
        return sum([self.aces, self.twos, self.threes,
                    self.fours, self.fives, self.sixes])

    @property
    def bonus(self):
        """Score for bonus.

        Returns:
            bonus score (int)
        """
        if self.bonus_earned:
            return 35
        else:
            return 0

    @property
    def bonus_earned(self):
        """Determine if bonus for upper section has been earned.

        Returns:
            subtotal earned (bool)
        """
        return  self.subtotal >= 63

    @property
    def total(self):
        """Total score including all categories and bonus.

        Returns:
            _total (int)
        """
        if self.bonus_earned:
            self._total = self.subtotal + 35
        else:
            self._total = self.subtotal
        return self._total
