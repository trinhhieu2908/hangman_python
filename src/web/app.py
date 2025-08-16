"""
Flask Application Factory

Creates and configures the Flask application instance.
This follows the application factory pattern for better organization.
"""

from flask import Flask
from .routes import hangman_bp


def create_app() -> Flask:
    """
    Create and configure Flask application.
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__, 
                template_folder='../../templates',
                static_folder='../../static')
    
    # Configure app
    app.config['SECRET_KEY'] = 'dylan-hangman-flask'
    app.config['DEBUG'] = True  # Remove in production
    
    # Register blueprints
    app.register_blueprint(hangman_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
