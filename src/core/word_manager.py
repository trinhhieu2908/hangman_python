"""
Word Dictionary Manager

Class-based word dictionary management for hangman game.
Provides caching and optimized word selection based on difficulty level.
"""

import os
import random
from typing import List, Optional


class WordManager:
    def __init__(self):
        """Initialize the word manager with empty caches."""
        self._basic_words_cache: Optional[List[str]] = None
        self._intermediate_phrases_cache: Optional[List[str]] = None

        # Get paths relative to the project root
        current_dir = os.path.dirname(__file__)
        project_root = os.path.join(current_dir, "..", "..")
        self._basic_words_path = os.path.join(project_root, "static", "basic_words.txt")
        self._intermediate_phrases_path = os.path.join(
            project_root, "static", "intermediate_phrases.txt"
        )

    def _load_words_from_file(self, file_path: str) -> List[str]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dictionary file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]

        return words

    def get_basic_words(self) -> List[str]:
        if self._basic_words_cache is None:
            self._basic_words_cache = self._load_words_from_file(self._basic_words_path)

        return self._basic_words_cache

    def get_intermediate_phrases(self) -> List[str]:
        if self._intermediate_phrases_cache is None:
            self._intermediate_phrases_cache = self._load_words_from_file(
                self._intermediate_phrases_path
            )

        return self._intermediate_phrases_cache

    def get_random_word(self, level: str) -> str:
        if level == "basic":
            words = self.get_basic_words()
            return random.choice(words).upper()
        elif level == "intermediate":
            phrases = self.get_intermediate_phrases()
            return random.choice(phrases).upper()
        else:
            raise ValueError(
                f"Invalid level: {level}. Must be 'basic' or 'intermediate'"
            )

    def clear_cache(self):
        self._basic_words_cache = None
        self._intermediate_phrases_cache = None


_word_manager = WordManager()


def get_random_word(level: str) -> str:
    return _word_manager.get_random_word(level)
