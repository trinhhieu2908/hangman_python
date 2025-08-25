"""
Tests for Word Manager

Tests for loading and managing word dictionaries.
"""

import pytest
from src.core.word_manager import WordManager


class TestWordManager:
    def test_get_basic_words_loads_successfully(self):
        """Test that basic words load from file."""
        word_manager = WordManager()
        words = word_manager.get_basic_words()
        assert isinstance(words, list)
        assert len(words) > 0
        # Check some expected words
        assert 'python' in [word.lower() for word in words]
        assert 'coding' in [word.lower() for word in words]

    def test_get_intermediate_phrases_loads_successfully(self):
        """Test that intermediate phrases load from file."""
        word_manager = WordManager()
        phrases = word_manager.get_intermediate_phrases()
        assert isinstance(phrases, list)
        assert len(phrases) > 0
        # Check some expected phrases
        phrase_list = [phrase.lower() for phrase in phrases]
        assert 'break a leg' in phrase_list
        assert 'piece of cake' in phrase_list

    def test_get_random_word_basic_level(self):
        """Test getting random basic word."""
        word_manager = WordManager()
        word = word_manager.get_random_word('basic')
        assert isinstance(word, str)
        assert len(word) > 0
        assert word.isupper()  # Should be uppercase
        assert ' ' not in word  # Should be single word

    def test_get_random_word_intermediate_level(self):
        """Test getting random intermediate phrase."""
        word_manager = WordManager()
        phrase = word_manager.get_random_word('intermediate')
        assert isinstance(phrase, str)
        assert len(phrase) > 0
        assert phrase.isupper()  # Should be uppercase

    def test_get_random_word_invalid_level(self):
        """Test that invalid level raises ValueError."""
        word_manager = WordManager()
        with pytest.raises(ValueError) as exc_info:
            word_manager.get_random_word('invalid')
        assert "Invalid level" in str(exc_info.value)
