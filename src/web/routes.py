"""
Web Routes for Hangman Game
"""

from flask import Blueprint, render_template, abort, request, jsonify
from src.utils.constants import DIFFICULTY_LEVELS, VALID_LETTERS
from src.core.game_engine import GameEngine

# Create blueprint for web routes
hangman_bp = Blueprint("hangman", __name__)
global_game_engine = GameEngine("basic")


@hangman_bp.route("/")
def home():
    """
    Home page with welcome message.

    Displays the welcome message and provides navigation to start the game.
    """
    return render_template("home.html")


@hangman_bp.route("/select-level")
def select_level():
    """
    Level selection page.

    Allows player to choose between Basic (words) and Intermediate (phrases).
    """
    return render_template("select_level.html", DIFFICULTY_LEVELS=DIFFICULTY_LEVELS)


@hangman_bp.route("/game/<level>")
def game(level):
    """
    Main game interface.

    Creates a new GameEngine instance for the selected level.
    Each page load starts a fresh game.
    """
    # Validate level
    if level not in ["basic", "intermediate"]:
        abort(404)

    # Create new game instance
    global global_game_engine
    global_game_engine = GameEngine(level)
    game_state = global_game_engine.get_game_state()

    return render_template(
        "game.html", game_state=game_state, valid_letters=VALID_LETTERS, level=level
    )


@hangman_bp.route("/guess", methods=["POST"])
def guess_letter():
    """
    Process a letter guess using the GameEngine.
    Game state is passed via request and returned updated.
    """
    data = request.get_json()
    letter = data.get("letter", "").upper()

    if not letter or letter not in VALID_LETTERS:
        return jsonify({"error": "Invalid letter"}), 400

    # Process the guess
    result = global_game_engine.guess_letter(letter)

    # Check if word is completed
    word_completion = global_game_engine.process_word_completion()

    # Return updated game state
    return jsonify(
        {
            "success": True,
            "result": result,
            "word_completion": word_completion,
            "game_state": global_game_engine.get_game_state(),
        }
    )
