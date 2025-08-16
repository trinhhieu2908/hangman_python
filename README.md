# Hangman Game

A classic word guessing game implemented in Python using Test-Driven Development (TDD) principles.

## Project Structure

```
hangman_dylan/
├── src/                    # Source code
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── tests/                  # Unit tests
├── docs/                   # Documentation
├── requirements.txt        # Project dependencies
├── setup.cfg              # Configuration for tools
├── .pylintrc              # Pylint configuration
├── .gitignore             # Git ignore rules
├── run_web_app.py         # Web application runner
├── README.md              # This file
└── run_web_app.py         # Web application runner

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
- Write comprehensive docstrings for all classes and methods

## Current Status

✅ **Minimal modular structure** created  
✅ **Flask web application** with clean architecture  
✅ **Welcome page** with modern, responsive design  
✅ **YAGNI principle** applied - only what's needed  
✅ **Integration test** for web interface  
✅ **Code quality tools** configured and passing  
⏳ **Game logic implementation** (upcoming - TDD approach)  
⏳ **Core functionality** (upcoming - tests first)

## Git Workflow

This project is ready for version control with Git:

### **Initial Setup:**

```bash
# Initialize repository
git init

# Add all files (gitignore will handle exclusions)
git add .

# Initial commit
git commit -m "Initial project structure with Flask web app"

# Add remote repository (replace with your repo URL)
git remote add origin https://github.com/username/hangman-game.git

# Push to remote
git push -u origin main
```

### **Development Workflow:**

```bash
# Create feature branch for TDD development
git checkout -b feature/game-logic

# Make changes, add tests, implement features
git add .
git commit -m "Add game logic with TDD approach"

# Push feature branch
git push origin feature/game-logic

# Merge when ready
git checkout main
git merge feature/game-logic
```

## Next Steps

1. **Implement core game logic** using TDD approach
2. **Add game state management** with session handling
3. **Create game page** with letter selection interface
4. **Add hangman drawing** visualization
5. **Implement word selection** and validation
6. **Add game completion** logic and statistics
