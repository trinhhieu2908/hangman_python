"""
Tests for GameEngine

Tests the core hangman game mechanics with continuous scoring system.
Players score points by completing words and game continues until lives = 0.
Follows TDD approach.
"""

import pytest
from src.core.game_engine import GameEngine


class TestGameCreation:
    def test_create_new_game_basic_level(self):
        """Test creating a new basic level game."""
        game = GameEngine(level='basic')
        
        assert game.level == 'basic'
        assert isinstance(game.word, str)
        assert len(game.word) > 0
        assert game.guessed_letters == []
        assert game.wrong_guesses == []
        assert game.lives == 6
        assert game.game_over == False
        assert game.score == 0  # Start with 0 score

    def test_create_new_game_intermediate_level(self):
        """Test creating a new intermediate level game."""
        game = GameEngine(level='intermediate')
        
        assert game.level == 'intermediate'
        assert isinstance(game.word, str)
        assert len(game.word) > 0
        assert game.score == 0

    def test_create_game_invalid_level(self):
        """Test that invalid level raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            GameEngine(level='invalid')
        assert "Invalid level" in str(exc_info.value)


class TestLetterGuessing:
    def test_guess_correct_letter(self):
        """Test guessing a correct letter."""
        game = GameEngine(level='basic')
        game.word = 'PYTHON'
        
        result = game.guess_letter('P')
        
        assert result['correct'] == True
        assert 'P' in game.guessed_letters
        assert game.lives == 6  # No life lost

    def test_guess_wrong_letter(self):
        """Test guessing a wrong letter."""
        game = GameEngine(level='basic')
        game.word = 'PYTHON'
        
        result = game.guess_letter('Z')
        
        assert result['correct'] == False
        assert 'Z' in game.guessed_letters
        assert 'Z' in game.wrong_guesses
        assert game.lives == 5  # Life lost


class TestScoringAndWordCompletion:
    """Test continuous scoring and word completion mechanics."""

    def test_word_completion_increases_score(self):
        """Test that completing a word increases score and resets state."""
        game = GameEngine(level='basic')
        game.word = 'CAT'
        game.guessed_letters = ['C', 'A', 'T']
        initial_score = game.score
        
        result = game.process_word_completion()
        
        assert result['word_completed'] == True
        assert result['completed_word'] == 'CAT'
        assert game.score == initial_score + 1
        assert game.guessed_letters == []  # Reset
        assert game.wrong_guesses == []   # Reset
        assert game.lives == 6            # Reset

    def test_incomplete_word_no_score(self):
        """Test that incomplete word doesn't trigger scoring."""
        game = GameEngine(level='basic')
        game.word = 'CAT'
        game.guessed_letters = ['C', 'A']  # Missing T
        initial_score = game.score
        
        result = game.process_word_completion()
        
        assert result['word_completed'] == False
        assert game.score == initial_score  # No change
        assert len(game.guessed_letters) == 2  # No reset

    def test_phrase_completion(self):
        """Test word completion with phrases (ignoring spaces)."""
        game = GameEngine(level='intermediate')
        game.word = 'BREAK A LEG'
        game.guessed_letters = ['B', 'R', 'E', 'A', 'K', 'L', 'G']
        
        result = game.process_word_completion()
        
        assert result['word_completed'] == True
        assert result['completed_word'] == 'BREAK A LEG'

class TestGameOverConditions:
    """Test game over conditions in continuous play."""

    def test_check_game_over_no_lives(self):
        """Test game over when no lives remaining."""
        game = GameEngine(level='basic')
        game.lives = 0
        
        assert game.check_game_over() == True

    def test_check_game_over_continuous_play(self):
        """Test game continues even after completing words."""
        game = GameEngine(level='basic')
        game.word = 'CAT'
        game.guessed_letters = ['C', 'A', 'T']
        game.lives = 6
        
        # Word complete but game continues (not over)
        assert game.check_game_over() == False

    def test_check_game_over_in_progress(self):
        """Test game continues when still in progress."""
        game = GameEngine(level='basic')
        game.word = 'CAT'
        game.guessed_letters = ['C', 'A']  # Still missing T
        game.lives = 3
        
        assert game.check_game_over() == False


class TestGameState:
    """Test game state information retrieval."""

    def test_get_game_state_basic(self):
        """Test getting complete game state information."""
        game = GameEngine(level='basic')
        game.word = 'PYTHON'
        game.guessed_letters = ['P', 'Y']
        game.wrong_guesses = ['Z']
        game.lives = 5
        game.score = 3
        
        state = game.get_game_state()
        
        assert state['word_display'] == 'PY____'
        assert state['guessed_letters'] == ['P', 'Y']
        assert state['wrong_guesses'] == ['Z']
        assert state['lives'] == 5
        assert state['game_over'] == False
        assert state['score'] == 3
        assert state['level'] == 'basic'
        assert state['word'] == 'PYTHON'

    def test_get_game_state_with_phrase(self):
        """Test game state with phrase containing spaces."""
        game = GameEngine(level='intermediate')
        game.word = 'BREAK A LEG'
        game.guessed_letters = ['B', 'R', 'E']
        game.score = 1
        
        state = game.get_game_state()
        
        assert state['word_display'] == 'BRE__ _ _E_'  # E appears in both BREAK and LEG
        assert state['level'] == 'intermediate'
        assert state['word'] == 'BREAK A LEG'
        assert state['score'] == 1

    def test_multiple_guesses_integration(self):
        """Test complete game flow with multiple guesses and scoring."""
        game = GameEngine(level='basic')
        game.word = 'CAT'
        initial_score = game.score
        
        # Guess correct letter
        result1 = game.guess_letter('C')
        assert result1['correct'] == True
        
        # Guess wrong letter
        result2 = game.guess_letter('Z')
        assert result2['correct'] == False
        assert game.lives == 5
        
        # Complete the word
        game.guess_letter('A')
        game.guess_letter('T')
        
        # Check word completion
        completion = game.process_word_completion()
        assert completion['word_completed'] == True
        assert game.score == initial_score + 1
        
        # Game should continue with new word
        state = game.get_game_state()
        assert state['game_over'] == False
        assert state['lives'] == 6  # Reset
        assert state['guessed_letters'] == []  # Reset