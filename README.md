# Hangman Game

A classic word guessing game implemented in Python using Test-Driven Development (TDD) principles.

## Project Structure

```
hangman_dylan/
├── src/                    # Source code
│   ├── core/               # Game logic and functions
│   ├── web/                # Web interface (Flask)
│   └── utils/              # Utilities and helpers
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── tests/                  # Unit tests
├── docs/                   # Documentation
├── requirements.txt        # Project dependencies
├── setup.cfg              # Configuration for tools
├── .pylintrc              # Pylint configuration
├── .gitignore             # Git ignore rules
├── run_web_app.py         # Web application runner
└── README.md              # This file
```

## Setup Instructions

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Web Application:**

   ```bash
   python run_web_app.py
   # Then open http://localhost:3001 in your browser
   ```

3. **Run Tests:**

   ```bash
   python -m pytest tests/ -v
   ```

4. **Code Quality Checks:**

   ```bash
   # Run pylint
   pylint src/

   # Run flake8
   flake8 src/

   # Run with coverage
   python -m pytest tests/ --cov=src --cov-report=html
   ```

## Development Guidelines

- Follow TDD principles: Write tests first, then implement functionality
- Maintain code quality using pylint and flake8
- Use type hints for better code documentation
- Follow PEP 8 style guidelines

## Current Status

✅ **Minimal modular structure** created  
✅ **Flask web application** with clean architecture  
✅ **Welcome page** with modern layout
✅ **Integration test** for web interface  
✅ **Code quality tools** configured and passing  
✅ **Game logic implementation** implemented test and logic
✅ **Core functionality** implemented test and logic
⏳ **Responsive layout** (upcoming)
