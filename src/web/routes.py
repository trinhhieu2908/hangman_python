"""
Web Routes for Hangman Game

Simple routes for the hangman game web interface.
Currently implements only the home page.
"""

from flask import Blueprint, render_template

# Create blueprint for web routes
hangman_bp = Blueprint('hangman', __name__)


@hangman_bp.route('/')
def home():
    """
    Home page with welcome message.
    
    Displays the welcome message and provides navigation to start the game.
    For now, this is the only implemented route.
    
    Returns:
        str: Rendered home template
    """
    return render_template('home.html')
