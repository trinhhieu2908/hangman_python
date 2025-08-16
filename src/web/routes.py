"""
Web Routes for Hangman Game
"""

from flask import Blueprint, render_template

# Create blueprint for web routes
hangman_bp = Blueprint('hangman', __name__)


@hangman_bp.route('/')
def home():
    """
    Home page with welcome message.
    
    Displays the welcome message and provides navigation to start the game.
    """
    return render_template('home.html')


@hangman_bp.route('/select-level')
def select_level():
    """
    Level selection page.
    
    Allows player to choose between Basic (words) and Intermediate (phrases).
    """
    return render_template('select_level.html')
