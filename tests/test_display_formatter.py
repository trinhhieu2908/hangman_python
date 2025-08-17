"""
Tests for Display Formatter

Tests for word display formatting with underscores.
Follows TDD approach - these tests should FAIL initially.
"""

import pytest
from src.utils.display_formatter import (
    format_word_display,
    format_lives_display
)


class TestWordDisplay:
    """Test word display with underscores."""

    def test_format_word_display_no_guesses(self):
        """Test display shows all underscores initially."""
        word = 'PYTHON'
        guessed_letters = []
        
        result = format_word_display(word, guessed_letters)
        assert result == '______'

    def test_format_word_display_with_spaces(self):
        """Test display preserves spaces in phrases."""
        word = 'BREAK A LEG'
        guessed_letters = []
        
        result = format_word_display(word, guessed_letters)
        assert result == '_____ _ ___'

    def test_format_word_display_partial_guesses(self):
        """Test display shows correctly guessed letters."""
        word = 'PYTHON'
        guessed_letters = ['P', 'O']
        
        result = format_word_display(word, guessed_letters)
        assert result == 'P___O_'

    def test_format_word_display_complete(self):
        """Test display shows complete word when all letters guessed."""
        word = 'CAT'
        guessed_letters = ['C', 'A', 'T']
        
        result = format_word_display(word, guessed_letters)
        assert result == 'CAT'

    def test_format_word_display_phrase_partial(self):
        """Test display with phrases and partial guesses."""
        word = 'HELLO WORLD'
        guessed_letters = ['H', 'L', 'O']
        
        result = format_word_display(word, guessed_letters)
        assert result == 'H_LLO _O_L_'


class TestLivesDisplay:
    """Test lives display formatting."""

    def test_format_lives_display_full_lives(self):
        """Test lives display with full hearts."""
        result = format_lives_display(6)
        assert result == '❤️❤️❤️❤️❤️❤️'

    def test_format_lives_display_partial_lives(self):
        """Test lives display with partial hearts."""
        result = format_lives_display(3)
        assert result == '❤️❤️❤️🤍🤍🤍'

    def test_format_lives_display_no_lives(self):
        """Test lives display with no hearts."""
        result = format_lives_display(0)
        assert result == '🤍🤍🤍🤍🤍🤍'
