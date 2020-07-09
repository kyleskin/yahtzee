"""Represents a Single Die."""

from random import randint


class Die:
    """Represent a Single Die.

    Attributes:
        name (str) = the name you give the die
        max_value (int) = the max value of the die
        value (int) = the current value of the die (the number showing up)
    """

    def __init__(self, name: str, max_value: int):
        """Create die with a name and max value.

        Parameters:
            name (str) = the name you give the die
            max_value (int) = the max value of the die
        """
        self._name = name
        self._max_value = max_value
        self._value = max_value

    @property
    def name(self) -> str:
        """Get die's name.
        
        Returns:
            _name (str)
        """
        return self._name

    @name.setter
    def name(self, new_name: str):
        """Set die's name.
        
        Parameters:
            new_name (str): the dice's new name
        """
        self._name = new_name

    @property
    def max_value(self) -> int:
        """Get die's max value.
        
        Returns:
            _max_value (int)
        """
        return self._max_value

    @property
    def value(self) -> int:
        """Get the die's current value, i.e. what has been rolled.
        
        Returns:
            _value (int)
        """
        return self._value

    @value.setter
    def value(self, new_value: int):
        """Set the die's current value.
        
        Parameters:
            new_value (int): The updatd current value for the die
        """
        if (new_value > self.max_value):
            raise ValueError("This value is higher than the die's max value")
        self._value = new_value

    def roll(self):
        """Simulate rolling the die.
        
        Selects a randint between 1 and the die's max value
        """
        self.value = randint(1, self.max_value)

    def __lt__(self, other: Die) -> bool:
        """Order dice according to their value.
        
        Returns:
            (bool)
        """
        return self.value < other.value

    def __str__(self) -> str:
        """Print out the die's value.

        If value is less than 6, ascii art will be displayed,
        if over 6, a string representing the value.

        Returns:
            (str)
        """
        art = [".---------.\n" +
               "|         |\n" +
               "|    O    |\n" +
               "|         |\n" +
               "'---------'\n",
               ".---------.\n" +
               "|  O      |\n" +
               "|         |\n" +
               "|      O  |\n" +
               "'---------'\n",
               ".---------.\n" +
               "|  O      |\n" +
               "|    O    |\n" +
               "|      O  |\n" +
               "'---------'\n",
               ".---------.\n" +
               "|  O   O  |\n" +
               "|         |\n" +
               "|  O   O  |\n" +
               "'---------'\n",
               ".---------.\n" +
               "|  O   O  |\n" +
               "|    O    |\n" +
               "|  O   O  |\n" +
               "'---------'\n",
               ".---------.\n" +
               "|  O   O  |\n" +
               "|  O   O  |\n" +
               "|  O   O  |\n" +
               "'---------'\n"]
        if self.value > len(art):
            return f'Value: {self.value}'
        return art[self.value - 1]
