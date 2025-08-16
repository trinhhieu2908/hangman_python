"""
Tests for Word Manager

Tests for loading and managing word dictionaries.
"""

import pytest
from src.core.word_manager import (
    get_basic_words,
    get_intermediate_phrases,
    get_random_word
)


class TestWordManager:
    def test_get_basic_words_loads_successfully(self):
        """Test that basic words load from file."""
        words = get_basic_words()
        assert isinstance(words, list)
        assert len(words) > 0
        # Check some expected words
        assert 'python' in [word.lower() for word in words]
        assert 'coding' in [word.lower() for word in words]

    def test_get_intermediate_phrases_loads_successfully(self):
        """Test that intermediate phrases load from file."""
        phrases = get_intermediate_phrases()
        assert isinstance(phrases, list)
        assert len(phrases) > 0
        # Check some expected phrases
        phrase_list = [phrase.lower() for phrase in phrases]
        assert 'break a leg' in phrase_list
        assert 'piece of cake' in phrase_list

    def test_basic_words_are_single_words(self):
        """Test that basic level contains only single words."""
        words = get_basic_words()
        for word in words:
            # Basic words should not contain spaces
            assert ' ' not in word.strip()
            # Should be reasonable length (4-15 characters for programming terms)
            assert 4 <= len(word.strip()) <= 15

    def test_intermediate_phrases_contain_multiple_words(self):
        """Test that intermediate level contains phrases with multiple words."""
        phrases = get_intermediate_phrases()
        multi_word_count = 0
        for phrase in phrases:
            words_in_phrase = phrase.strip().split()
            if len(words_in_phrase) > 1:
                multi_word_count += 1
        
        # Most phrases should have multiple words
        assert multi_word_count > len(phrases) * 0.8  # At least 80% should be multi-word

    def test_get_random_word_basic_level(self):
        """Test getting random basic word."""
        word = get_random_word('basic')
        assert isinstance(word, str)
        assert len(word) > 0
        assert word.isupper()  # Should be uppercase
        assert ' ' not in word  # Should be single word

    def test_get_random_word_intermediate_level(self):
        """Test getting random intermediate phrase."""
        phrase = get_random_word('intermediate')
        assert isinstance(phrase, str)
        assert len(phrase) > 0
        assert phrase.isupper()  # Should be uppercase

    def test_get_random_word_invalid_level(self):
        """Test that invalid level raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            get_random_word('invalid')
        assert "Invalid level" in str(exc_info.value)
