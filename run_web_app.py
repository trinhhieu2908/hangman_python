"""
Web Application Runner

Simple script to run the Flask web application.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.web.app import create_app

if __name__ == "__main__":
    app = create_app()
    print("🎯 Starting Hangman Web Application...")
    print("🌐 Open your browser and go to: http://localhost:3001")
    print("🛑 Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=3001)
