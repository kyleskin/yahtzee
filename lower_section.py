"""Represents the lower section of the Yahtzee scorecard.

Includes 3 of a kind, 4 of a kind, full house, small straight,
large straight, yahtzee, chance, and yahtzee bonus.
"""

from collections import defaultdict
import errors
# import dice

class LowerSection:
    """Represents the lower section of the Yahtzee scorecard.

    Attributes:
        _three_kind (int) = score for 3 of a kind
        _three_kind_scored (bool) = if 3 of a kind has been scored yet
        _four_kind (int) = score for 4 of a kind
        _four_kind_scored (bool) = if 4 of a kind has been scored yet
        _full_house (int) = score for full house
        _full_house_scored (bool) = if full house has been scored yet
        _small_straight (int) = score for small straight
        _small_straight_scored (bool) = if small straight has been scored yet
        _large_straight (int) = score for large straight
        _large_straight_scored (bool) = if large straight has been scored yet
        _yahtzee (int) = score for yahtzee
        _num_yahtzee_bonus (int) = number of yahtzee bonuses that have been earned
        _yahtzee_bonus (int) = score for yahtzee bonuses
        _yahtzee_scored (bool) = if yahtzee has been scored yet
        _chance (int) = score for chance
        _chance_scored (bool) = if chance has been scored yet
        _total (int) = total score for the lower section
    """

    def __init__(self):
        """Set up lower section of scorecard - all values zeroed out."""
        self._three_kind = 0
        self._three_kind_scored = False
        self._four_kind = 0
        self._four_kind_scored = False
        self._full_house = 0
        self._full_house_scored = False
        self._small_straight = 0
        self._small_straight_scored = False
        self._large_straight = 0
        self._large_straight_scored = False
        self._yahtzee = 0
        self._num_yatzhee_bonus = 0
        self._yahtzee_bonus = 0
        self._yahtzee_scored = False
        self._chance = 0
        self._chance_scored = False
        self._total = 0

    @property
    def three_kind(self) -> int:
        """Get score for 3 of a kind.
        
        Returns:
            _three_kind (int)
        """
        return self._three_kind

    @three_kind.setter
    def three_kind(self, dice: Dice):
        """Score 3 of a kind.
            
        Parameters:
            dice (Dice) = the dice to be scored
        """
        if self.three_kind_scored:
            raise errors.AlreadyScored
        else:
            # Determine if there are 3 matching dice
            three_of_a_kind = False
            d = defaultdict(int)
            for die in dice:
                d[die.value] += 1
            for key, value in d.items():
                if value >= 3:
                    three_of_a_kind = True
            
            if three_of_a_kind:
                # Add up values for all dice
                self._three_kind = sum(die.value for die in dice)
            self.three_kind_scored = True

    @property
    def three_kind_scored(self) -> bool:
        """Determine if 3 of a kind has been scored already.
        
        Returns:
            _three_kind_scored (bool)
        """
        return self._three_kind_scored

    @three_kind_scored.setter
    def three_kind_scored(self, scored: bool):
        """Set if 3 of kind has been scored.

        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._three_kind_scored = scored

    @property
    def four_kind(self) -> int:
        """Get score for 4 of a kind.
        
        Returns:
            _four_kind (int)
        """
        return self._four_kind

    @four_kind.setter
    def four_kind(self, dice: Dice):
        """Score for 4 of a kind.
        
        Parameters:
            dice (Dice) = the dice to be scored
        """
        if self.four_kind_scored:
            raise errors.AlreadyScored
        else:
            # Determine if there are 3 matching dice
            four_of_a_kind = False
            d = defaultdict(int)
            for die in dice:
                d[die.value] += 1
            for key, value in d.items():
                if value >= 4:
                    four_of_a_kind = True
            
            if four_of_a_kind:
                # Add up values for all dice
                self._four_kind = sum(die.value for die in dice)
            self.four_kind_scored = True

    @property
    def four_kind_scored(self) -> bool:
        """Determine if 4 of a kind has been scored already.
        
        Returns:
            _four_kind_scored (bool)
        """
        return self._four_kind_scored

    @four_kind_scored.setter
    def four_kind_scored(self, scored: bool):
        """Set if 4 of kind has been scored.
        
        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._four_kind_scored = scored

    @property
    def full_house(self) -> int:
        """Get score for full house.
        
        Returns:
            _full_house (int)
        """
        return self._full_house

    @full_house.setter
    def full_house(self, dice: Dice):
        """Score full house.
        
        Parameters:
            dice (Dice) = the dice to be scored
        """
        if self.full_house_scored:
            raise errors.AlreadyScored
        else:
            # Determine if dice count for full house
            two_of_a_kind = False
            three_of_a_kind = False
            d = defaultdict(int)
            for die in dice:
                d[die.value] += 1
            for key, value in d.items():
                if value == 2:
                    two_of_a_kind = True
                if value == 3:
                    three_of_a_kind = True
            if two_of_a_kind and three_of_a_kind:
                self._full_house = 25
            self.full_house_scored = True
    
    @property
    def full_house_scored(self) -> bool:
        """Determine if full house has been scored already.
        
        Returns:
            _full_house_scored (bool)
        """
        return self._full_house_scored
    
    @full_house_scored.setter
    def full_house_scored(self, scored: bool):
        """Set if full house has been scored.
        
        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._full_house_scored = scored

    @property
    def small_straight(self) -> int:
        """Get score for small straight.
        
        Returns:
            _small_straight (int)
        """
        return self._small_straight

    @small_straight.setter
    def small_straight(self, dice: Dice):
        """Score small straight.
        
        Parameters:
            dice (Dice) = the dice to be scored
        """
        # 3 possible small straights
        s1 = {1, 2, 3, 4}
        s2 = {2, 3, 4, 5}
        s3 = {3, 4, 5, 6}
        if self.small_straight_scored:
            raise errors.AlreadyScored
        else:
            values = set([die.value for die in dice])
            # Determine if dice match any of the possible small straights
            if s1.issubset(values) or s2.issubset(values) or s3.issubset(values):
                self._small_straight = 30
            self.small_straight_scored = True

    @property
    def small_straight_scored(self) -> bool:
        """Determine if small straight has been scored already.
        
        Returns:
            _small_straight_scored (bool)
        """
        return self._small_straight_scored

    @small_straight_scored.setter
    def small_straight_scored(self, scored):
        """Set if small straight has been scored.
        
        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._small_straight_scored = scored

    @property
    def large_straight(self) -> int:
        """Get score for large straight.
        
        Returns:
            _large_straight (int)
        """
        return self._large_straight

    @large_straight.setter
    def large_straight(self, dice: Dice):
        """Score large straight.
        
        Parameters:
            dice (Dice) = the dice to be scored
        """
        # 2 possible large straights
        s1 = {1, 2, 3, 4, 5}
        s2 = {2, 3, 4, 5, 6}
        if self.large_straight_scored:
            raise errors.AlreadyScored
        else:
            values = set([die.value for die in dice])
            # Determine if dice match either of the possible large straights
            if s1.issubset(values) or s2.issubset(values):
                self._large_straight = 40
            self.large_straight_scored = True

    @property
    def large_straight_scored(self) -> bool:
        """Determine if large straight has been scored already.
        
        Returns:
            _large_straight_scored (bool)
        """
        return self._large_straight_scored

    @large_straight_scored.setter
    def large_straight_scored(self, scored: bool):
        """Set if large straight has been scored.
        
        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._large_straight_scored = scored

    @property
    def yahtzee(self) -> int:
        """Get score for yahtzee.
        
        Returns:
            _yahtzee (int)
        """
        return self._yahtzee

    @yahtzee.setter
    def yahtzee(self, dice: Dice):
        """Score yahtzee.
        
        Parameters:
            dice (Dice) = the dice to be scored
        """
        # Determine if dice count as a yahtzee
        is_yahtzee = False
        d = defaultdict(int)
        for die in dice:
            d[die.value] += 1

        for key, value in d.items():
            if value == 5:
                is_yahtzee = True

        # Determine if dice should count as yahtzee or bonus or nothing
        if not self.yahtzee_scored and not is_yahtzee:
            self.yahtzee_scored = True
        elif not self.yahtzee_scored and is_yahtzee:
            self.yahtzee_scored = True
            self._yahtzee = 50
        elif self.yahtzee_scored and not is_yahtzee:
            raise errors.AlreadyScored
        else:
            if self.yahtzee == 0:
                raise errors.AlreadyScored
            else:
                self.num_yahtzee_bonus += 1

    @property
    def yahtzee_scored(self) -> bool:
        """Determine if yahtzee has been scored already.
        
        Returns:
            _yahtzee_scored (bool)
        """
        return self._yahtzee_scored

    @yahtzee_scored.setter
    def yahtzee_scored(self, scored: bool):
        """Set if yahtzee is scored already.
        
        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._yahtzee_scored = scored

    @property
    def num_yahtzee_bonus(self) -> int:
        """Get number of yahtzee bonuses.
        
        Returns:
            _num_yahtzee_bonus (int)
        """
        return self._num_yatzhee_bonus

    @num_yahtzee_bonus.setter
    def num_yahtzee_bonus(self, i: int):
        """Set the number of yahtzee bonuses.
        
        Parameters:
            i (int) = number of yahtzee bonuses scored
        """
        self._num_yatzhee_bonus = i

    @property
    def yahtzee_bonus(self) -> int:
        """Get score of yahtzee bonuses.
        
        Returns:
            (int)
        """
        return self.num_yahtzee_bonus * 100

    @property
    def chance(self) -> int:
        """Get score for chance.
        
        Returns:
            _chance (int)
        """
        return self._chance

    @chance.setter
    def chance(self, dice: Dice):
        """Score chance.
        
        Parameters:
            dice (Dice) = the dice to be scored
        """
        if self.chance_scored:
            raise errors.AlreadyScored
        else:
            self._chance = sum(die.value for die in dice)
        self.chance_scored = True

    @property
    def chance_scored(self) -> bool:
        """Determine if chance has been scored already.
        
        Returns:
            _chance_scored (bool)
        """
        return self._chance_scored
    
    @chance_scored.setter
    def chance_scored(self, scored: bool):
        """Set if chance has been scored.
        
        Parameters:
            scored (bool) = whether the category has been scored
        """
        self._chance_scored = scored

    @property
    def total(self) -> int:
        """Get the total score for the lower section.
        
        Returns:
            (int)
        """
        return sum([self.three_kind, self.four_kind, self.full_house,
                    self.small_straight, self.large_straight,
                    self.yahtzee, self.yahtzee_bonus, self.chance])
