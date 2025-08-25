"""
Game Engine

Core hangman game mechanics and state management.
"""

from typing import Dict, Any
from .word_manager import get_random_word
from ..utils.constants import MAX_LIVES, GAME_MESSAGES
from ..utils.display_formatter import format_word_display, format_lives_display


class GameEngine:
    def __init__(self, level: str):
        if level not in ["basic", "intermediate"]:
            raise ValueError(
                f"Invalid level: {level}. Must be 'basic' or 'intermediate'"
            )

        # Game configuration
        self.level = level
        self.word = get_random_word(level)

        # Player progress
        self.guessed_letters = []
        self.wrong_guesses = []
        self.lives = MAX_LIVES

        # Game status - continuous play with scoring
        self.game_over = False
        self.score = 0

    def get_game_state(self) -> Dict[str, Any]:
        self.game_over = self.check_game_over()
        word_display = format_word_display(self.word, self.guessed_letters)
        lives_display = format_lives_display(self.lives)

        return {
            "word_display": word_display,
            "guessed_letters": self.guessed_letters,
            "wrong_guesses": self.wrong_guesses,
            "lives": self.lives,
            "game_over": self.game_over,
            "score": self.score,
            "level": self.level,
            "word": self.word,  # For answer reveal when game over
            "lives_display": lives_display,
        }

    def guess_letter(self, letter: str) -> Dict[str, Any]:
        # Convert to uppercase for consistency
        letter = letter.upper()

        # Check for duplicate guess
        if letter in self.guessed_letters:
            return {"correct": False, "message": GAME_MESSAGES["duplicate_guess"]}

        # Add to guessed letters
        self.guessed_letters.append(letter)

        # Check if letter is in word
        if self._is_letter_in_word(letter):
            # Correct guess
            return {"correct": True, "message": GAME_MESSAGES["correct_guess"]}
        else:
            self.wrong_guesses.append(letter)
            self.lives -= 1

            return {"correct": False, "message": GAME_MESSAGES["wrong_guess"]}

    def check_game_over(self) -> bool:
        return self.lives <= 0

    def process_word_completion(self) -> Dict[str, Any]:
        if self._is_word_complete():
            self.score += 1
            completed_word = self.word
            self._reset_for_new_word()
            return {
                "word_completed": True,
                "completed_word": completed_word,
                "score": self.score,
                "message": GAME_MESSAGES["correct_word"],
            }
        return {"word_completed": False}

    def _is_letter_in_word(self, letter: str) -> bool:
        # Spaces are not letters
        if letter == " ":
            return False

        return letter.upper() in self.word.upper()

    def _is_word_complete(self) -> bool:
        """Check if current word is fully guessed."""
        for char in self.word:
            if char != " " and char not in self.guessed_letters:
                return False
        return True

    def _reset_for_new_word(self):
        """Reset game state for a new word while keeping score."""
        self.word = get_random_word(self.level)
        self.guessed_letters = []
        self.wrong_guesses = []
        self.lives = MAX_LIVES
