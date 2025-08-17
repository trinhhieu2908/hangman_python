"""
Display Formatter

Pure utility functions for formatting hangman game displays.
"""

from typing import List
from .constants import UNDERSCORE_PLACEHOLDER, MAX_LIVES


def format_word_display(word: str, guessed_letters: List[str]) -> str:
    # Convert guessed letters to uppercase for comparison
    guessed_upper = [letter.upper() for letter in guessed_letters]

    result = ""

    for char in word:
        if char == " ":
            # Preserve spaces as-is
            result += " "
        elif char.upper() in guessed_upper:
            # Show guessed letters
            result += char
        else:
            # Show underscore for unguessed letters
            result += UNDERSCORE_PLACEHOLDER

    return result


def format_lives_display(lives: int, max_lives: int = MAX_LIVES) -> str:
    # Red hearts for remaining lives
    filled_hearts = "❤️" * lives
    # White hearts for lost lives
    empty_hearts = "🤍" * (max_lives - lives)

    return filled_hearts + empty_hearts
