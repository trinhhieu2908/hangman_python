"""
Game Constants

Central location for all hangman game configuration values.
This prevents magic numbers scattered throughout the codebase.
"""

# Game Lives Configuration
MAX_LIVES = 6  # Standard hangman lives (head, body, 2 arms, 2 legs)

# Timer Configuration
TIMER_SECONDS = 15  # Time limit per guess in seconds
TIMER_WARNING_THRESHOLD = 5  # Show warning when timer reaches this value

# Game Status Messages
GAME_MESSAGES = {
    "correct_guess": "Good guess!",
    "wrong_guess": "Wrong letter!",
    "duplicate_guess": "Letter already guessed!",
    "timeout": "Time is up!",
    "correct_word": "Word completed! Great job!",
    "game_over": "Game Over! Final Score: {}",
    "keep_guessing": "Keep guessing! {} lives remaining.",
    "last_life": "Last chance! Be careful!",
}

# Display Configuration
UNDERSCORE_PLACEHOLDER = "_"
LETTER_SEPARATOR = " "

# Difficulty Levels
DIFFICULTY_LEVELS = {
    "basic": {
        "name": "Basic Level",
        "description": "Single words only",
        "max_word_length": 15,
        "min_word_length": 4,
    },
    "intermediate": {
        "name": "Intermediate Level",
        "description": "Complete phrases",
        "max_words": 4,
        "min_words": 2,
    },
}

# Valid input characters
VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
