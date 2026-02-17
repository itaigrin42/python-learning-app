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
    # Build-In Funcions (built-in functions - matches notebook topic name)
    QuizQuestion(
        question="What does sum([1, 2, 3, 4]) return?",
        options=["10", "1234", "Error", "4"],
        correct_index=0,
        topic="Build-In Funcions",
        explanation="sum() adds all elements in an iterable: 1+2+3+4 = 10."
    ),
    QuizQuestion(
        question="What does range(5) produce?",
        options=["[0,1,2,3,4]", "0,1,2,3,4", "A range object (0 to 4)", "[1,2,3,4,5]"],
        correct_index=2,
        topic="Build-In Funcions",
        explanation="range(5) returns a range object that yields 0,1,2,3,4 when iterated."
    ),
    QuizQuestion(
        question="What does max([3, 1, 4, 1, 5]) return?",
        options=["1", "3", "5", "14"],
        correct_index=2,
        topic="Build-In Funcions",
        explanation="max() returns the largest value in the iterable."
    ),
    QuizQuestion(
        question="What does sorted([3, 1, 2]) return?",
        options=["[3, 1, 2]", "[1, 2, 3]", "(1, 2, 3)", "Error"],
        correct_index=1,
        topic="Build-In Funcions",
        explanation="sorted() returns a new list with elements in ascending order."
    ),
    QuizQuestion(
        question="What does str(42) return?",
        options=["42", "'42'", "Error", "42.0"],
        correct_index=1,
        topic="Build-In Funcions",
        explanation="str() converts a value to a string: str(42) gives '42'."
    ),
    QuizQuestion(
        question="What does round(3.7) return?",
        options=["3", "4", "3.7", "3.0"],
        correct_index=1,
        topic="Build-In Funcions",
        explanation="round() rounds to the nearest integer; 3.7 rounds to 4."
    ),
    QuizQuestion(
        question="What does abs(-10) return?",
        options=["-10", "10", "0", "Error"],
        correct_index=1,
        topic="Build-In Funcions",
        explanation="abs() returns the absolute value (distance from zero)."
    ),
    QuizQuestion(
        question="What does enumerate(['a','b']) produce when converted to list?",
        options=["['a','b']", "[(0,'a'),(1,'b')]", "[0,1]", "Error"],
        correct_index=1,
        topic="Build-In Funcions",
        explanation="enumerate() yields (index, value) pairs for each element."
    ),
    # Classes
    QuizQuestion(
        question="What keyword defines a class in Python?",
        options=["class", "def", "struct", "type"],
        correct_index=0,
        topic="Classes",
        explanation="Use 'class ClassName:' to define a class."
    ),
    QuizQuestion(
        question="What is the first parameter of an instance method?",
        options=["cls", "self", "this", "me"],
        correct_index=1,
        topic="Classes",
        explanation="By convention, 'self' refers to the instance."
    ),
    QuizQuestion(
        question="What does __init__ do?",
        options=["Initializes the class", "Initializes a new instance", "Imports the module", "Inherits from parent"],
        correct_index=1,
        topic="Classes",
        explanation="__init__ is the constructor that runs when creating a new instance."
    ),
    QuizQuestion(
        question="What does __str__ define?",
        options=["String representation for developers", "User-friendly string when printing", "Strict type checking", "String concatenation"],
        correct_index=1,
        topic="Classes",
        explanation="__str__ returns a readable string used by print() and str()."
    ),
    QuizQuestion(
        question="A class attribute is shared by:",
        options=["Only one instance", "All instances of the class", "Only child classes", "No instances"],
        correct_index=1,
        topic="Classes",
        explanation="Class attributes are shared across all instances."
    ),
    # Files
    QuizQuestion(
        question="Which function opens a file for reading?",
        options=["read()", "open()", "load()", "file()"],
        correct_index=1,
        topic="Files",
        explanation="open(filename, 'r') opens a file for reading."
    ),
    QuizQuestion(
        question="What does 'r' mode mean when opening a file?",
        options=["Replace", "Read", "Run", "Return"],
        correct_index=1,
        topic="Files",
        explanation="'r' opens the file in read-only mode."
    ),
    QuizQuestion(
        question="What should you do after opening a file?",
        options=["Nothing", "Close it with .close() or use 'with'", "Delete it", "Rename it"],
        correct_index=1,
        topic="Files",
        explanation="Always close files to free resources; 'with' does this automatically."
    ),
    QuizQuestion(
        question="What does file.readline() return?",
        options=["The whole file", "One line as a string", "A list of lines", "The file size"],
        correct_index=1,
        topic="Files",
        explanation="readline() reads and returns a single line."
    ),
    QuizQuestion(
        question="Which mode allows writing without overwriting?",
        options=["'w'", "'a'", "'r'", "'x'"],
        correct_index=1,
        topic="Files",
        explanation="'a' is append mode - adds to the end without erasing."
    ),
    # loop through files
    QuizQuestion(
        question="What does os.listdir(path) return?",
        options=["File contents", "List of filenames in directory", "File size", "Error"],
        correct_index=1,
        topic="loop through files",
        explanation="listdir() returns a list of entry names in the directory."
    ),
    QuizQuestion(
        question="Which module is used for path operations?",
        options=["os", "pathlib", "sys", "Both os and pathlib"],
        correct_index=3,
        topic="loop through files",
        explanation="Both os and pathlib can handle file paths."
    ),
    QuizQuestion(
        question="What does Path.glob('*.txt') do?",
        options=["Opens all txt files", "Finds all .txt files in the directory", "Deletes txt files", "Renames txt files"],
        correct_index=1,
        topic="loop through files",
        explanation="glob() matches filenames by pattern."
    ),
    # Matplotlib 1
    QuizQuestion(
        question="What does plt.plot(x, y) do?",
        options=["Creates a bar chart", "Creates a line plot", "Saves the figure", "Shows the plot"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="plot() creates a line plot by default."
    ),
    QuizQuestion(
        question="What does plt.show() do?",
        options=["Saves the figure", "Displays the plot window", "Closes the plot", "Clears the axes"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="show() displays the figure to the screen."
    ),
    QuizQuestion(
        question="Which creates a bar chart?",
        options=["plt.plot()", "plt.bar()", "plt.line()", "plt.chart()"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="plt.bar(x, height) creates a bar chart."
    ),
    QuizQuestion(
        question="What does plt.xlabel() set?",
        options=["The title", "The x-axis label", "The legend", "The y-axis label"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="xlabel() sets the label for the x-axis."
    ),
    # Matplotlib 2
    QuizQuestion(
        question="What does plt.subplot(2, 1, 1) create?",
        options=["2 rows, 1 column, select first", "2 columns, 1 row", "2 figures", "1x1 grid"],
        correct_index=0,
        topic="Matplotlib 2",
        explanation="subplot(rows, cols, index) creates a grid and selects one."
    ),
    QuizQuestion(
        question="What does plt.figure(figsize=(10, 5)) do?",
        options=["Creates 10 subplots", "Sets figure size to 10x5 inches", "Sets DPI", "Creates 5 figures"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="figsize=(width, height) in inches."
    ),
    QuizQuestion(
        question="Which adds a legend to the plot?",
        options=["plt.title()", "plt.legend()", "plt.label()", "plt.caption()"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="legend() displays the legend for labeled lines."
    ),
    # Matplotlib Exercise - plt.text
    QuizQuestion(
        question="What does plt.text(x, y, 'label') do?",
        options=["Adds a title", "Adds text at coordinates (x,y)", "Adds x and y labels", "Adds a legend"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="text() places a string at the given coordinates."
    ),
    QuizQuestion(
        question="What does plt.annotate() add?",
        options=["Only text", "Text with an optional arrow", "A new subplot", "A colorbar"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="annotate() adds text with optional arrow pointing to a point."
    ),
    # Pandas & Matplotlib
    QuizQuestion(
        question="What does df.plot() create?",
        options=["A table", "A visualization of the DataFrame", "A new DataFrame", "Nothing"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="DataFrame.plot() creates charts from the data."
    ),
    QuizQuestion(
        question="Which creates a histogram from a column?",
        options=["df.plot()", "df['col'].hist()", "df.bar()", "df.chart()"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="Series.hist() creates a histogram."
    ),
    QuizQuestion(
        question="What does kind='bar' do in df.plot()?",
        options=["Creates a line plot", "Creates a bar chart", "Creates a scatter plot", "Creates a pie chart"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="kind='bar' specifies a bar chart."
    ),
    # Pandas 2
    QuizQuestion(
        question="What does df.groupby('col') do?",
        options=["Sorts by column", "Groups rows by column values", "Deletes the column", "Renames the column"],
        correct_index=1,
        topic="Pandas 2",
        explanation="groupby() splits the DataFrame by unique values."
    ),
    QuizQuestion(
        question="What does .agg(['mean', 'sum']) do?",
        options=["Filters rows", "Applies multiple aggregations", "Merges DataFrames", "Drops columns"],
        correct_index=1,
        topic="Pandas 2",
        explanation="agg() applies aggregation functions to groups."
    ),
    QuizQuestion(
        question="What does df.pivot_table() create?",
        options=["A long-format table", "A summary table with rows/columns", "A copy of df", "A merged DataFrame"],
        correct_index=1,
        topic="Pandas 2",
        explanation="pivot_table() reshapes and aggregates data."
    ),
    # Pandas 3
    QuizQuestion(
        question="What does pd.merge(df1, df2) do?",
        options=["Concatenates vertically", "Joins DataFrames on columns", "Replaces df1 with df2", "Duplicates rows"],
        correct_index=1,
        topic="Pandas 3",
        explanation="merge() joins two DataFrames (like SQL JOIN)."
    ),
    QuizQuestion(
        question="What does pd.concat([df1, df2]) do by default?",
        options=["Merges on a key", "Stacks DataFrames vertically", "Creates a cross product", "Takes the union of columns"],
        correct_index=1,
        topic="Pandas 3",
        explanation="concat() stacks along axis=0 (rows) by default."
    ),
    QuizQuestion(
        question="What does the 'on' parameter in merge() specify?",
        options=["Output filename", "Column(s) to join on", "Sort order", "Number of rows"],
        correct_index=1,
        topic="Pandas 3",
        explanation="'on' names the key column(s) for the join."
    ),
    # Variables & DataTypes (alternate spelling from notebook)
    QuizQuestion(
        question="What type is 3.14?",
        options=["int", "float", "str", "bool"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="Numbers with decimals are float type."
    ),
    QuizQuestion(
        question="What does bool(0) return?",
        options=["True", "False", "0", "Error"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="Zero is falsy; bool(0) is False."
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
