"""
Word Dictionary Manager

Handles loading and selecting words/phrases for hangman game.
Provides functions to get random words based on difficulty level.
"""

import os
import random
from typing import List


def load_words_from_file(file_path: str) -> List[str]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dictionary file not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    
    return words


def get_basic_words() -> List[str]:
    """
    Load basic level words (single words, 4-15 letters).
    """
    # Get the path relative to the project root
    current_dir = os.path.dirname(__file__)
    project_root = os.path.join(current_dir, '..', '..')
    file_path = os.path.join(project_root, 'static', 'basic_words.txt')
    
    return load_words_from_file(file_path)


def get_intermediate_phrases() -> List[str]:
    """
    Load intermediate level phrases (2-4 words per phrase).
    """
    # Get the path relative to the project root
    current_dir = os.path.dirname(__file__)
    project_root = os.path.join(current_dir, '..', '..')
    file_path = os.path.join(project_root, 'static', 'intermediate_phrases.txt')
    
    return load_words_from_file(file_path)


def get_random_word(level: str) -> str:
    """
    Get a random word or phrase based on difficulty level.
    """
    if level == 'basic':
        words = get_basic_words()
        return random.choice(words).upper()
    elif level == 'intermediate':
        phrases = get_intermediate_phrases()
        return random.choice(phrases).upper()
    else:
        raise ValueError(f"Invalid level: {level}. Must be 'basic' or 'intermediate'")
