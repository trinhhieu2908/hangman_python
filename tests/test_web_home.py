"""
Tests for Web Home Page

Follows TDD principles.
"""

import sys
import os

# Add src directory to path for importing modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from src.web.app import create_app


class TestWebHome:
    @pytest.fixture
    def client(self):
        """Create test client."""
        app = create_app()
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client
    
    def test_home_page_loads_successfully(self, client):
        """Test that home page loads without errors."""
        response = client.get('/')
        assert response.status_code == 200
        assert "Start Game" in response.get_data(as_text=True)
    
    def test_start_game_button_redirects_to_level_selection(self, client):
        """Test that Start Game button links to level selection page."""
        # Get home page
        response = client.get('/')
        assert response.status_code == 200
        
        # Check that the Start Game button has correct href
        html_content = response.get_data(as_text=True)
        assert 'href="/select-level"' in html_content
