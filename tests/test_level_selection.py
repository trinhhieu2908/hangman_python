"""
Test Level Selection Functionality
"""

import pytest
from src.web.app import create_app


class TestLevelSelection:
    """Test class for level selection functionality."""

    @pytest.fixture
    def client(self):
        app = create_app()
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_level_selection_page_loads(self, client):
        """Test that level selection page loads successfully."""
        response = client.get('/select-level')
        assert response.status_code == 200
        assert b'Choose Your Challenge' in response.data

    def test_level_selection_contains_basic_option(self, client):
        """Test that level selection page contains Basic option."""
        response = client.get('/select-level')
        assert b'Basic Level' in response.data
        assert b'individual words' in response.data

    def test_level_selection_contains_intermediate_option(self, client):
        """Test that level selection page contains Intermediate option."""
        response = client.get('/select-level')
        assert b'Intermediate Level' in response.data
        assert b'complete phrases' in response.data

    def test_level_selection_contains_back_to_home_button(self, client):
        """Test that level selection page contains Back to Home button."""
        response = client.get('/select-level')
        assert b'Back to Home' in response.data
