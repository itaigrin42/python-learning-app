"""
Parser for Jupyter notebooks - extracts questions and code exercises.
"""
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class Exercise:
    """A single exercise from a notebook."""
    topic: str
    question_num: int
    title: str
    instructions: str
    hint_code: Optional[str] = None  # Code shown in markdown (example/hint)
    solution_code: Optional[str] = None  # Code from code cell
    notebook_name: str = ""


def _join_source(cell_source: list) -> str:
    """Join notebook cell source (list of strings) into one string."""
    if not cell_source:
        return ""
    return "".join(cell_source).strip()


def _extract_code_from_markdown(text: str) -> Optional[str]:
    """Extract Python code from markdown code blocks."""
    if "```python" not in text:
        return None
    parts = text.split("```python")
    if len(parts) < 2:
        return None
    code_block = parts[1].split("```")[0].strip()
    return code_block if code_block else None


def parse_notebook(filepath: Path) -> list[Exercise]:
    """
    Parse a Jupyter notebook and extract exercises.
    Handles: markdown (question) -> code (solution) pairs.
    """
    exercises = []
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return exercises

    cells = nb.get("cells", [])
    topic = filepath.stem.replace("- Questions", "").replace(" - h.w", "").replace(" Questions", "")
    
    # Clean topic name (e.g., "1. Variables & DataTypes" -> "Variables & DataTypes")
    if topic[0].isdigit() and ". " in topic:
        topic = topic.split(". ", 1)[1]
    
    i = 0
    question_num = 0
    
    while i < len(cells):
        cell = cells[i]
        cell_type = cell.get("cell_type", "")
        source = _join_source(cell.get("source", []))
        
        # Skip empty cells
        if not source:
            i += 1
            continue
            
        # Skip copyright/attribution
        if "©" in source or "Advanced Analytics" in source:
            i += 1
            continue
            
        # Skip short header-only cells (e.g., "## Seaborn", "# Classes", "### Load file")
        stripped = source.strip()
        if cell_type == "markdown" and stripped.startswith("#") and len(stripped) < 60 and "\n" not in stripped:
            i += 1
            continue
        # Skip "Topic\n\n## Questions" intro cells
        if cell_type == "markdown" and "## Questions" in source and len(source) < 150:
            i += 1
            continue
        if cell_type == "markdown" and "Let's start by importing" in source and len(source) < 100:
            i += 1
            continue
            
        # Look for markdown that seems like a question
        if cell_type == "markdown":
            # Check if next cell is code
            next_source = ""
            next_code = ""
            if i + 1 < len(cells):
                next_cell = cells[i + 1]
                if next_cell.get("cell_type") == "code":
                    next_source = _join_source(next_cell.get("source", []))
                    next_code = next_source if next_source else None
            
            question_num += 1
            
            # Extract title (## header, **Exercise**, or first meaningful line)
            lines = source.split("\n")
            title = ""
            for line in lines:
                line = line.strip()
                if line.startswith("##"):
                    title = line.replace("#", "").strip()
                    break
                if line.startswith("**Exercise") or line.startswith("**"):
                    title = line.replace("**", "").strip()
                    break
                if line and not line.startswith("-") and "```" not in line:
                    title = line[:80] + ("..." if len(line) > 80 else "")
                    break
            
            hint_code = _extract_code_from_markdown(source)
            
            ex = Exercise(
                topic=topic,
                question_num=question_num,
                title=title or f"Exercise {question_num}",
                instructions=source,
                hint_code=hint_code,
                solution_code=next_code if next_code else None,
                notebook_name=filepath.name
            )
            exercises.append(ex)
            
            # Skip the next code cell if we used it
            if i + 1 < len(cells) and cells[i + 1].get("cell_type") == "code":
                i += 2
            else:
                i += 1
        else:
            i += 1

    return exercises


def discover_notebooks(directory: Path) -> list[Path]:
    """Find all question notebooks in directory."""
    notebooks = []
    for path in directory.glob("*.ipynb"):
        if path.name.startswith("."):
            continue
        if "checkpoint" in path.name.lower():
            continue
        # Include Questions, h.w., and similar
        if "Questions" in path.name or "h.w" in path.name.lower():
            notebooks.append(path)
    return sorted(notebooks, key=lambda p: p.name.lower())


def load_all_exercises(directory: Path) -> dict[str, list[Exercise]]:
    """Load exercises from all notebooks, grouped by topic."""
    notebooks = discover_notebooks(directory)
    by_topic: dict[str, list[Exercise]] = {}
    
    for nb_path in notebooks:
        exercises = parse_notebook(nb_path)
        if exercises:
            topic = exercises[0].topic
            if topic not in by_topic:
                by_topic[topic] = []
            by_topic[topic].extend(exercises)
    
    return by_topic
