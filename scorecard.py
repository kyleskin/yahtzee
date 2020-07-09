"""Represents the player's scorecard, including upper and lower sections."""

import upper_section
import lower_section
import errors

class Scorecard:
    """Represents the player's scorecard, including upper and lower sections."""

    def __init__(self):
        """Player's scorecard, including upper and lower sections and the grand total.
            
        Attributes:
            _up (UpperSection) = the upper section of the scorecard
            _low (LowerSection) = the lower section of the scorecard
            _grand_total (int) = The total of both upper and lower sections

            aces = the score for aces or --- if not scored
            twos = the score for twos or --- if not scored
            threes = the score for threes or --- if not scored
            fours = the score for fours or --- if not scored
            fives = the score for fives or --- if not scored
            sixes = the score for sixes or --- if not scored
            three_kind = the score for 3 of a kind or --- if not scored
            four_kind = the score for 4 of a kind or --- if not scored
            full_house = the score for full house or --- if not scored
            small_straight = the score for small straight or --- if not scored
            large_straight = the score for large straight or --- if not scored
            yahtzee = the score for yahtzee or --- if not scored
            chance = the score for chance or --- if not scored
            num_yahtzee_bonus = the number of yahtzee bonuses or --- if none
            yahtzee_bonus = the score for yahtzee bonuses or --- if 0
        """
        self._up = upper_section.UpperSection()
        self._low = lower_section.LowerSection()
        self._grand_total = self.up.total + self.low.total

    @property
    def up(self):
        """Get the upper section of the scorecard.
        
        Returns:
            _up (UpperSection)
        """
        return self._up

    @property
    def low(self):
        """Get the lower section of the scorecard.
        
        Returns:
            _low (LowerSection)
        """
        return self._low

    @property
    def aces(self):
        """Get aces score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.up.aces_scored:
            return "---"
        else:
            return self.up.aces

    @property
    def twos(self):
        """Get twos score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.up.twos_scored:
            return "---"
        else:
            return self.up.twos

    @property
    def threes(self):
        """Get threes score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.up.threes_scored:
            return "---"
        else:
            return self.up.threes

    @property
    def fours(self):
        """Get fours score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.up.fours_scored:
            return "---"
        else:
            return self.up.fours

    @property
    def fives(self):
        """Get fives score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.up.fives_scored:
            return "---"
        else:
            return self.up.fives

    @property
    def sixes(self):
        """Get sixes score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.up.sixes_scored:
            return "---"
        else:
            return self.up.sixes

    @property
    def three_kind(self):
        """Get 3 of a kind score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.three_kind_scored:
            return "---"
        else:
            return self.low.three_kind

    @property
    def four_kind(self):
        """Get four of a kind score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.four_kind_scored:
            return "---"
        else:
            return self.low.four_kind

    @property
    def full_house(self):
        """Get full house score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.full_house_scored:
            return "---"
        else:
            return self.low.full_house

    @property
    def small_straight(self):
        """Get small straight score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.small_straight_scored:
            return "---"
        else:
            return self.low.small_straight

    @property
    def large_straight(self):
        """Get large straight score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.large_straight_scored:
            return "---"
        else:
            return self.low.large_straight

    @property
    def yahtzee(self):
        """Get yahtzee score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.yahtzee_scored:
            return "---"
        else:
            return self.low.yahtzee

    @property
    def chance(self):
        """Get chance score or --- if not scored.
        
        Returns:
            (str or int)
        """
        if not self.low.chance_scored:
            return "---"
        else:
            return self.low.chance

    @property
    def num_yahtzee_bonus(self):
        """Get number of yahtzee bonuses or --- if none.
        
        Returns:
            (str or int)
        """
        if self.low.num_yahtzee_bonus == 0:
            return "---"
        else:
            return self.low.num_yahtzee_bonus

    @property
    def yahtzee_bonus(self):
        """Get yahtzee bonuses score or --- if no bonuses.
        
        Returns:
            (str or int)
        """
        if self.low.num_yahtzee_bonus == 0:
            return "---"
        else:
            return self.low.yahtzee_bonus

    @property
    def grand_total(self):
        """Get grand total of upper and lower sections.
        
        Returns:
            (int)
        """
        return self.up.total + self.low.total

    def score(self, selection, dice):
        """Score the selected category.

        Parameters:
            selection (str) = which category is to be scored
            dice (Dice) = the dice
        """
        selections = ["a", "b", "c", "d", "e", "f", "g",
                      "h", "i", "j", "k", "l", "m"]
        if selection not in selections:
            raise errors.InvalidSelection
        if selection == "a":
            self.up.aces = dice
        elif selection == "b":
            self.up.twos = dice
        elif selection == "c":
            self.up.threes = dice
        elif selection == "d":
            self.up.fours = dice
        elif selection == "e":
            self.up.fives = dice
        elif selection == "f":
            self.up.sixes = dice
        elif selection == "g":
            self.low.three_kind = dice
        elif selection == "h":
            self.low.four_kind = dice
        elif selection == "i":
            self.low.full_house = dice
        elif selection == "j":
            self.low.small_straight = dice
        elif selection == "k":
            self.low.large_straight = dice
        elif selection == "l":
            self.low.yahtzee = dice
        elif selection == "m":
            self.low.chance = dice

    def __str__(self):
        """Print out the scorecard with selections and category scores."""
        s = ("  Upper Section" + 
             "\n  [a] " + "Aces".center(14) + ":" + f"{self.aces}".center(6) +
             "\n  [b] " + "Twos".center(14) + ":" + f"{self.twos}".center(6) +
             "\n  [c] " + "Threes".center(14) + ":" + f"{self.threes}".center(6) +
             "\n  [d] " + "Fours".center(14) + ":" + f"{self.fours}".center(6) +
             "\n  [e] " + "Fives".center(14) + ":" + f"{self.fives}".center(6) +
             "\n  [f] " + "Sixes".center(14) + ":" + f"{self.sixes}".center(6) +
             "\n      " + "SubTotal".center(14) + ":" + f"{self.up.subtotal}".center(6) +
             "\n      " + "Bonus".center(14) + ":" + f"{self.up.bonus}".center(6) +
             "\n      " + "Total".center(14) + ":" + f"{self.up.total}".center(6) +
             "\n  Lower Section" +
             "\n  [g] " + "3 of a Kind".center(14) + ":" + f"{self.three_kind}".center(6) +
             "\n  [h] " + "4 of a Kind".center(14) + ":" + f"{self.four_kind}".center(6) +
             "\n  [i] " + "Full House".center(14) + ":" + f"{self.full_house}".center(6) +
             "\n  [j] " + "Small Straight".center(14) + ":" + f"{self.small_straight}".center(6) +
             "\n  [k] " + "Large Straight".center(14) + ":" + f"{self.large_straight}".center(6) +
             "\n  [l] " + "Yahtzee".center(14) + ":" + f"{self.yahtzee}".center(6) +
             "\n  [m] " + "Chance".center(14) + ":" + f"{self.chance}".center(6) +
             "\n      " + "Yahtzee Bonus".center(14) + ":" + f"{self.num_yahtzee_bonus}".center(6) +
             "\n      " + "Bonus Points".center(14) + ":" + f"{self.yahtzee_bonus}".center(6) +
             "\n      " + "Lower Total".center(14) + ":" + f"{self.low.total}".center(6) +
             "\n      " + "Upper Total".center(14) + ":" + f"{self.up.total}".center(6) +
             "\n      " + "Grand Total".center(14) + ":" + f"{self.grand_total}".center(6)
        )
        return s

