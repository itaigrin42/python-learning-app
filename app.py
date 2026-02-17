"""
Entry point for Streamlit Cloud deployment.
Runs the Python Learning App from python_learning_app/.
"""
import sys
from pathlib import Path

# Ensure the app package is importable
sys.path.insert(0, str(Path(__file__).parent))

from python_learning_app.app import main

if __name__ == "__main__":
    main()
