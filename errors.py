"""Exceptions to be used in Yahtzee."""

class AlreadyScored(Exception):
    """Raised when a category already has a scored recorded for it."""

    pass

class InvalidSelection(Exception):
    """Raised when a selection is not available."""
    
    pass