"""
Tests for Game UI

Tests the main hangman game interface, routes, and session management.
Follows TDD approach.
"""

import pytest
from src.web.app import create_app


class TestGameRoute:
    """Test game route and initialization."""

    @pytest.fixture
    def client(self):
        app = create_app()
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_game_route_basic_level(self, client):
        """Test game route loads for basic level."""
        response = client.get('/game/basic')
        assert response.status_code == 200
        
        html_content = response.get_data(as_text=True)
        assert 'hangman-game' in html_content
        assert 'word-display' in html_content
        assert 'gallows' in html_content
        assert 'basic' in html_content

    def test_game_route_intermediate_level(self, client):
        """Test game route loads for intermediate level."""
        response = client.get('/game/intermediate')
        assert response.status_code == 200
        
        html_content = response.get_data(as_text=True)
        assert 'hangman-game' in html_content
        assert 'intermediate' in html_content

    def test_game_route_invalid_level(self, client):
        """Test game route returns 404 for invalid level."""
        response = client.get('/game/expert')
        assert response.status_code == 404

    def test_game_ui_contains_virtual_keyboard(self, client):
        """Test game UI contains virtual keyboard with all letters."""
        response = client.get('/game/basic')
        html_content = response.get_data(as_text=True)
        
        # Check for keyboard container
        assert 'virtual-keyboard' in html_content
        
        # Check for all letters A-Z
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            assert f'data-letter="{letter}"' in html_content

    def test_game_ui_contains_game_sections(self, client):
        """Test game UI contains required sections."""
        response = client.get('/game/basic')
        html_content = response.get_data(as_text=True)
        
        # Word display and gallows
        assert 'word-display' in html_content
        assert 'gallows' in html_content
        
        # Virtual keyboard
        assert 'virtual-keyboard' in html_content
        
        # Score display
        assert 'score' in html_content

    def test_game_ui_shows_initial_game_state(self, client):
        """Test game UI shows initial game state."""
        response = client.get('/game/basic')
        html_content = response.get_data(as_text=True)
        
        # Should show underscores for word
        assert '_' in html_content
        
        # Should show score 0
        assert 'Score: 0' in html_content
