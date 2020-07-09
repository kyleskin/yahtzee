"""Represents a collection of Dice."""

from die import Die


class Dice:
    """Represents a Collection of Dice.

    Attributes:
        col_width (int): how wide each column should be
        fill (str): string used to fill in between header columns
        divider (str): string used to divide the columns
        dice (List[Die]): list of dice.
    """

    def __init__(self,
                 col_width=9,
                 fill='-',
                 divider='||',
                 dice=[Die("Die 1", 6), Die("Die 2", 6)]):
        """
        Represent a collection of dice.

        Parameters:
            col_width (int): how wide each column should be
            fill (str): string used to fill in between header columns
            divider (str): string used to divide the columns
            dice (List[Die]): list of dice, default is two six-sided dice
        """
        self._dice = dice
        self.column_width = col_width
        self.fill_char = fill
        self.divider_char = divider

    @property
    def dice(self):
        """List of dice.

        Returns:
            _dice (List[Die])
        """
        return self._dice

    def __getitem__(self, index):
        """Return die at index.

        Returns:
            (die)
        """
        return self.dice[index]

    def __iter__(self) -> Die:
        """Return iterable object of dice.

        Returns:
            (iter)
        """
        return iter(self.dice)

    def __len__(self):
        """Return length of the list of dice.

        Returns:
            (int)
        """
        return len(self.dice)

    def format_header(self):
        """Format the header.

        A dividing string will appear between each column
        and a fill string will also be used in each column.

        Returns:
            (str): the formatted header using the dice names in columns
        """
        header = ''

        for die in self.dice[:-1]:
            # Print the DIVIDER character after each column except the last one
            header += (die.name.center(self.column_width, self.fill_char)
                       + self.divider_char)
        # Print the last column without the DIVIDER character
        header += (self.dice[-1].name.center(self.column_width,
                                             self.fill_char))

        return header

    def format_rolls(self):
        """Format the list of dice rolls.

        A dividing string will appear between each column

        Returns:
            (str): the dice's value formatted into columns
        """
        result = ''
        for die in self.dice[:-1]:
            # Print the divider char after each column except the last one
            result += (str(die.value).center(self.column_width)
                       + self.divider_char)
        # Print the last column without the divider character after it
        result += (str(self.dice[-1].value).center(self.column_width))

        return result

    def roll(self):
        """Simulate rolling all the dice."""
        for die in self.dice:
            die.roll()

    def __str__(self):
        """Print header and latest results of rolling dice.

        Returns:
            str: formatted header and columns with the random rolls
        """
        result = self.format_header() + '\n' + self.format_rolls()
        return result
