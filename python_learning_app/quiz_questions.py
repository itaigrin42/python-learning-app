"""
American-style multiple choice quiz questions.
Topics: variables, data types, functions, control flow, lists, dicts.
No classes, files, or databases.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class QuizQuestion:
    question: str
    options: list[str]  # A, B, C, D
    correct_index: int  # 0-based
    topic: str
    explanation: Optional[str] = None


QUIZ_QUESTIONS: list[QuizQuestion] = [
    # Variables & Data Types
    QuizQuestion(
        question="What is the output of: print(type(42))?",
        options=["int", "integer", "number", "None"],
        correct_index=0,
        topic="Variables & Data Types",
        explanation="In Python, whole numbers are of type int."
    ),
    QuizQuestion(
        question="Which of the following is a valid variable name in Python?",
        options=["2nd_value", "my-var", "my_var", "for"],
        correct_index=2,
        topic="Variables & Data Types",
        explanation="Variable names cannot start with a number, cannot contain hyphens, and 'for' is a reserved keyword."
    ),
    QuizQuestion(
        question="What does len('hello') return?",
        options=["4", "5", "6", "Error"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="The string 'hello' has 5 characters."
    ),
    QuizQuestion(
        question="What is the result of 10 // 3?",
        options=["3.33", "3", "3.0", "4"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="// is floor division; it returns integer division (10 divided by 3 is 3 remainder 1)."
    ),
    QuizQuestion(
        question="Which operator checks if two values are equal?",
        options=["=", "==", "equals", ":="],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="== is the equality operator. = is for assignment."
    ),
    # Control Flow
    QuizQuestion(
        question="How many times will 'Hi' be printed? for i in range(3): print('Hi')",
        options=["0", "2", "3", "4"],
        correct_index=2,
        topic="Control Flow",
        explanation="range(3) produces 0, 1, 2, so the loop runs 3 times."
    ),
    QuizQuestion(
        question="What does the 'else' in a for loop do?",
        options=["Runs if the loop was broken", "Runs after every iteration", "Runs if the loop completes normally", "Runs only on the last iteration"],
        correct_index=2,
        topic="Control Flow",
        explanation="In Python, for-else runs the else block only if the loop completes without a break."
    ),
    QuizQuestion(
        question="What is the output? x = 5; print('Yes' if x > 3 else 'No')",
        options=["Yes", "No", "True", "Error"],
        correct_index=0,
        topic="Control Flow",
        explanation="x > 3 is True, so the ternary returns 'Yes'."
    ),
    QuizQuestion(
        question="Which loop is best for iterating over a list when you need the index?",
        options=["for item in list", "for i in range(len(list))", "while True", "Both A and B work equally well"],
        correct_index=1,
        topic="Control Flow",
        explanation="range(len(list)) gives you indices 0, 1, 2, ... to access list[i]."
    ),
    # Functions
    QuizQuestion(
        question="What does a function return if it has no return statement?",
        options=["0", "None", "Error", "The last expression evaluated"],
        correct_index=1,
        topic="Functions",
        explanation="Functions without a return statement implicitly return None."
    ),
    QuizQuestion(
        question="Which is the correct way to define a function with a default argument?",
        options=["def f(x=5)", "def f(x := 5)", "def f(x: 5)", "def f(x default 5)"],
        correct_index=0,
        topic="Functions",
        explanation="Default values use = in the parameter list: def f(x=5)."
    ),
    QuizQuestion(
        question="What does *args allow in a function?",
        options=["Multiple return values", "Variable number of positional arguments", "Optional arguments only", "Keyword arguments"],
        correct_index=1,
        topic="Functions",
        explanation="*args collects extra positional arguments into a tuple."
    ),
    QuizQuestion(
        question="Can a function call itself?",
        options=["No, never", "Yes, this is called recursion", "Only in loops", "Only with special syntax"],
        correct_index=1,
        topic="Functions",
        explanation="Recursion is when a function calls itself."
    ),
    # Data Structures (Lists, Dicts - no classes/files/DB)
    QuizQuestion(
        question="What does my_list.append(5) do?",
        options=["Adds 5 at index 0", "Adds 5 at the end", "Replaces the last element with 5", "Creates a new list with 5"],
        correct_index=1,
        topic="Data Structures",
        explanation="append() adds an element to the end of the list."
    ),
    QuizQuestion(
        question="What is my_list[-1]?",
        options=["First element", "Last element", "Error", "Length of list"],
        correct_index=1,
        topic="Data Structures",
        explanation="Negative indices count from the end; -1 is the last element."
    ),
    QuizQuestion(
        question="What does {'a': 1, 'b': 2}['c'] produce?",
        options=["None", "0", "KeyError", "Empty string"],
        correct_index=2,
        topic="Data Structures",
        explanation="Accessing a missing key raises KeyError. Use .get() for a default."
    ),
    QuizQuestion(
        question="What does [1, 2, 3][1:3] return?",
        options=["[1, 2]", "[2, 3]", "[1, 2, 3]", "[1, 3]"],
        correct_index=1,
        topic="Data Structures",
        explanation="Slicing [1:3] takes indices 1 and 2 (elements 2 and 3)."
    ),
    QuizQuestion(
        question="Which method removes and returns the last item from a list?",
        options=["remove()", "pop()", "delete()", "drop()"],
        correct_index=1,
        topic="Data Structures",
        explanation="pop() without arguments removes and returns the last element."
    ),
    QuizQuestion(
        question="What is the result of list('abc')?",
        options=["['a', 'b', 'c']", "['abc']", "Error", "abc"],
        correct_index=0,
        topic="Data Structures",
        explanation="list() converts an iterable (like a string) into a list of its elements."
    ),
]

def is_coding_safe_topic(topic: str) -> bool:
    """
    Check if a topic is safe for the coding section.
    Excludes: classes, files, databases (per user preference).
    """
    t = topic.strip().lower()
    if "class" in t or "file" in t or "database" in t:
        return False
    if t in ("files", "loop through files"):
        return False
    return True
