# Python Learning App

An interactive app that helps you practice Python using exercises from your Jupyter notebooks.

## Features

- **Browse by topic** – Automatically discovers and organizes notebooks (Variables, Classes, Seaborn, etc.)
- **Practice mode** – Hide solutions until you're ready to check
- **Hints** – View example code from the instructions
- **Try it yourself** – Optional code editor to experiment (for simpler exercises)

## Setup

```bash
cd python_learning_app
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

The app will scan the parent folder (`pyt/`) for notebooks with "Questions" or "h.w" in the filename and load their exercises.

## Supported notebooks

- `Classes - Questions - h.w.ipynb`
- `Seaborn - Questions.ipynb`
- `1. Variables & DataTypes - Questions - h.w.ipynb`
- `2. Data Structures - Questions- h.w.ipynb`
- `4. Control Flow - Questions - h.w.ipynb`
- `5. Functions - Questions - h.w.ipynb`
- `Pandas & Matplotlib - Questions.ipynb`
- And any other `*Questions*.ipynb` or `*h.w*.ipynb` files

## Note

For exercises that require data (e.g., Seaborn, Pandas), run the code in your Jupyter notebook where the data is loaded. The "Run code" feature works best for simple exercises (Variables, Classes, etc.).
