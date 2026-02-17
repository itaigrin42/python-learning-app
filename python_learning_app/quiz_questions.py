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
    QuizQuestion(
        question="What is the result of 'hello' + 'world'?",
        options=["'helloworld'", "'hello world'", "Error", "10"],
        correct_index=0,
        topic="Variables & Data Types",
        explanation="+ concatenates strings: 'hello' + 'world' = 'helloworld'."
    ),
    QuizQuestion(
        question="What does 'hello'[1:4] return?",
        options=["'hel'", "'ell'", "'llo'", "'hello'"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="Slicing [1:4] takes indices 1, 2, 3: 'e', 'l', 'l'."
    ),
    QuizQuestion(
        question="What is type(True)?",
        options=["int", "bool", "str", "None"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="True and False are of type bool."
    ),
    QuizQuestion(
        question="What does 2 ** 3 evaluate to?",
        options=["6", "8", "9", "23"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="** is exponentiation: 2**3 = 2*2*2 = 8."
    ),
    QuizQuestion(
        question="What is the result of 7 % 3?",
        options=["2", "2.33", "1", "3"],
        correct_index=0,
        topic="Variables & Data Types",
        explanation="% is modulo (remainder): 7 divided by 3 leaves remainder 2."
    ),
    QuizQuestion(
        question="Which creates an empty dictionary?",
        options=["[]", "{}", "()", "set()"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="{} creates an empty dict. [] is list, () is tuple, set() is empty set."
    ),
    QuizQuestion(
        question="What does int('42') return?",
        options=["'42'", "42", "42.0", "Error"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="int() converts a string to an integer."
    ),
    QuizQuestion(
        question="What is None?",
        options=["0", "An empty string", "A special value meaning 'no value'", "False"],
        correct_index=2,
        topic="Variables & Data Types",
        explanation="None is Python's null value, representing absence of a value."
    ),
    QuizQuestion(
        question="What does 'hi'.upper() return?",
        options=["'hi'", "'HI'", "'Hi'", "Error"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="upper() returns a copy with all characters uppercase."
    ),
    QuizQuestion(
        question="What does 'Hello'.lower() return?",
        options=["'Hello'", "'hello'", "'HELLO'", "Error"],
        correct_index=1,
        topic="Variables & Data Types",
        explanation="lower() returns a copy with all characters lowercase."
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
    QuizQuestion(
        question="What does break do in a loop?",
        options=["Skips to the next iteration", "Exits the loop immediately", "Pauses the loop", "Restarts the loop"],
        correct_index=1,
        topic="Control Flow",
        explanation="break exits the loop immediately, skipping any remaining iterations."
    ),
    QuizQuestion(
        question="What does continue do in a loop?",
        options=["Exits the loop", "Skips the rest of the current iteration", "Pauses execution", "Restarts from the beginning"],
        correct_index=1,
        topic="Control Flow",
        explanation="continue skips the rest of the current iteration and moves to the next."
    ),
    QuizQuestion(
        question="What is the output? for i in range(2, 5): print(i)",
        options=["2, 3, 4", "2, 3, 4, 5", "0, 1, 2, 3, 4", "2, 4"],
        correct_index=0,
        topic="Control Flow",
        explanation="range(2, 5) produces 2, 3, 4 (start inclusive, stop exclusive)."
    ),
    QuizQuestion(
        question="What does pass do?",
        options=["Exits the function", "Skips to the next statement", "Nothing - it's a placeholder", "Raises an error"],
        correct_index=2,
        topic="Control Flow",
        explanation="pass is a no-op placeholder for empty blocks."
    ),
    QuizQuestion(
        question="What is the output? x = 0; while x < 3: x += 1; print(x)",
        options=["1, 2, 3", "0, 1, 2", "1, 2, 3, 4", "0, 1, 2, 3"],
        correct_index=0,
        topic="Control Flow",
        explanation="x goes 0→1 (print 1), 1→2 (print 2), 2→3 (print 3), then 3 < 3 is False, loop stops."
    ),
    QuizQuestion(
        question="Which keyword is used for multiple conditions in an if statement?",
        options=["and", "or", "elif", "All of the above"],
        correct_index=3,
        topic="Control Flow",
        explanation="and/or combine conditions; elif handles else-if chains."
    ),
    QuizQuestion(
        question="What does range(0, 10, 2) produce?",
        options=["[0, 2, 4, 6, 8]", "0, 2, 4, 6, 8", "[0, 2, 4, 6, 8, 10]", "0, 2, 4, 6, 8, 10"],
        correct_index=1,
        topic="Control Flow",
        explanation="range(start, stop, step) yields 0, 2, 4, 6, 8 (step of 2)."
    ),
    QuizQuestion(
        question="What is the output? if False: print('A'); else: print('B')",
        options=["A", "B", "Nothing", "Error"],
        correct_index=1,
        topic="Control Flow",
        explanation="The if condition is False, so the else block runs and prints B."
    ),
    QuizQuestion(
        question="How do you write 'if x is not 5' in Python?",
        options=["if x != 5", "if not x == 5", "if x is not 5", "All of the above work"],
        correct_index=3,
        topic="Control Flow",
        explanation="!=, not x==5, and 'is not' (for identity) all express 'not equal' in different contexts."
    ),
    QuizQuestion(
        question="What does for i, x in enumerate(['a','b']): do?",
        options=["Loops with i=0,1 and x='a','b'", "Loops twice with x only", "Raises an error", "Loops with i='a','b'"],
        correct_index=0,
        topic="Control Flow",
        explanation="enumerate() yields (index, value) pairs: (0,'a'), (1,'b')."
    ),
    QuizQuestion(
        question="Which is the correct way to check if x is between 1 and 10 (inclusive)?",
        options=["1 <= x <= 10", "x >= 1 and x <= 10", "x in range(1, 11)", "All of the above"],
        correct_index=3,
        topic="Control Flow",
        explanation="Python supports chained comparisons (1<=x<=10), and/or, and range(1,11) for 1..10."
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
    QuizQuestion(
        question="What does **kwargs allow in a function?",
        options=["Multiple return values", "Variable keyword arguments", "Required arguments", "Positional arguments"],
        correct_index=1,
        topic="Functions",
        explanation="**kwargs collects extra keyword arguments into a dict."
    ),
    QuizQuestion(
        question="What is a lambda function?",
        options=["A long function", "An anonymous one-line function", "A function that returns None", "A recursive function"],
        correct_index=1,
        topic="Functions",
        explanation="lambda creates a small anonymous function: lambda x: x*2"
    ),
    QuizQuestion(
        question="What does return without a value do?",
        options=["Returns 0", "Returns None", "Raises an error", "Returns the last variable"],
        correct_index=1,
        topic="Functions",
        explanation="return with no value is equivalent to return None."
    ),
    QuizQuestion(
        question="Can a function have multiple return statements?",
        options=["No", "Yes, the first one reached runs", "Only in try/except", "Only with else"],
        correct_index=1,
        topic="Functions",
        explanation="Multiple returns are allowed; the first one executed exits the function."
    ),
    QuizQuestion(
        question="What does def f(a, b, *args): mean?",
        options=["a and b are optional", "args gets extra positional arguments", "args is a keyword", "Invalid syntax"],
        correct_index=1,
        topic="Functions",
        explanation="*args collects any extra positional arguments after a and b."
    ),
    QuizQuestion(
        question="What is the scope of a variable defined inside a function?",
        options=["Global", "Local to that function", "Module-level", "Persists after the function ends"],
        correct_index=1,
        topic="Functions",
        explanation="Variables defined in a function are local unless declared global."
    ),
    QuizQuestion(
        question="What does the global keyword do?",
        options=["Creates a global variable", "Allows modifying a variable from the outer scope", "Imports a module", "Defines a constant"],
        correct_index=1,
        topic="Functions",
        explanation="global x allows the function to modify the module-level variable x."
    ),
    QuizQuestion(
        question="What is the output of: (lambda x, y: x + y)(2, 3)?",
        options=["5", "23", "Error", "None"],
        correct_index=0,
        topic="Functions",
        explanation="The lambda adds 2 and 3, returning 5."
    ),
    QuizQuestion(
        question="What does a function's docstring do?",
        options=["Runs the function", "Documents the function (accessible via __doc__)", "Is required for every function", "Replaces the return value"],
        correct_index=1,
        topic="Functions",
        explanation="Docstrings document the function and are stored in __doc__."
    ),
    QuizQuestion(
        question="Can you pass a function as an argument to another function?",
        options=["No", "Yes, functions are first-class objects", "Only built-in functions", "Only with a wrapper"],
        correct_index=1,
        topic="Functions",
        explanation="Functions can be passed as arguments (e.g. to map, filter, sorted)."
    ),
    QuizQuestion(
        question="What does def f(): pass do?",
        options=["Defines an empty function", "Raises an error", "Returns pass", "Does nothing"],
        correct_index=0,
        topic="Functions",
        explanation="pass is a placeholder; the function does nothing but is valid."
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
    QuizQuestion(
        question="What does my_dict.get('key', 0) return if 'key' is missing?",
        options=["None", "0", "KeyError", "''"],
        correct_index=1,
        topic="Data Structures",
        explanation="get(key, default) returns the default when the key is missing."
    ),
    QuizQuestion(
        question="What does [1, 2] + [3, 4] produce?",
        options=["[1, 2, 3, 4]", "[4, 6]", "Error", "[1, 3, 2, 4]"],
        correct_index=0,
        topic="Data Structures",
        explanation="+ concatenates lists: [1,2] + [3,4] = [1,2,3,4]."
    ),
    QuizQuestion(
        question="What does my_list.insert(0, x) do?",
        options=["Replaces element at 0", "Inserts x at the beginning", "Appends x", "Removes element at 0"],
        correct_index=1,
        topic="Data Structures",
        explanation="insert(i, x) inserts x at index i, shifting elements right."
    ),
    QuizQuestion(
        question="What does {1, 2, 2, 3} create?",
        options=["A dict", "A list", "A set: {1, 2, 3}", "Error"],
        correct_index=2,
        topic="Data Structures",
        explanation="Curly braces with values (no colons) create a set; duplicates are removed."
    ),
    QuizQuestion(
        question="What does (1, 2)[1] return?",
        options=["1", "2", "Error", "(2)"],
        correct_index=1,
        topic="Data Structures",
        explanation="Tuples support indexing; index 1 is the second element."
    ),
    QuizQuestion(
        question="What does my_list.extend([1, 2]) do?",
        options=["Replaces the list", "Adds [1, 2] as one element", "Adds 1 and 2 to the end", "Inserts at index 0"],
        correct_index=2,
        topic="Data Structures",
        explanation="extend() adds each element from the iterable to the list."
    ),
    QuizQuestion(
        question="What does dict.keys() return?",
        options=["A list of keys", "A dict_keys view", "A tuple", "A set"],
        correct_index=1,
        topic="Data Structures",
        explanation="keys() returns a view object (updates with the dict)."
    ),
    QuizQuestion(
        question="What does [x*2 for x in range(3)] produce?",
        options=["[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]", "Error"],
        correct_index=0,
        topic="Data Structures",
        explanation="List comprehension: 0*2=0, 1*2=2, 2*2=4."
    ),
    QuizQuestion(
        question="What does {k: v for k, v in [('a',1),('b',2)]} produce?",
        options=["['a','b']", "{'a': 1, 'b': 2}", "Error", "[1, 2]"],
        correct_index=1,
        topic="Data Structures",
        explanation="Dict comprehension builds a dict from key-value pairs."
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
    QuizQuestion(
        question="What does min([3, 1, 4]) return?",
        options=["1", "3", "4", "8"],
        correct_index=0,
        topic="Build-In Funcions",
        explanation="min() returns the smallest value in the iterable."
    ),
    QuizQuestion(
        question="What does list(range(3)) produce?",
        options=["[0, 1, 2]", "[1, 2, 3]", "[0, 1, 2, 3]", "range(0, 3)"],
        correct_index=0,
        topic="Build-In Funcions",
        explanation="list() converts range(3) to [0, 1, 2]."
    ),
    QuizQuestion(
        question="What does zip([1,2], ['a','b']) produce when converted to list?",
        options=["[(1,'a'), (2,'b')]", "[[1,'a'], [2,'b']]", "[1, 2, 'a', 'b']", "Error"],
        correct_index=0,
        topic="Build-In Funcions",
        explanation="zip() pairs elements: (1,'a'), (2,'b')."
    ),
    QuizQuestion(
        question="What does map(lambda x: x*2, [1,2,3]) produce when converted to list?",
        options=["[2, 4, 6]", "[1, 2, 3]", "Error", "[1, 2, 3, 1, 2, 3]"],
        correct_index=0,
        topic="Build-In Funcions",
        explanation="map applies the function to each element: 1*2, 2*2, 3*2."
    ),
    QuizQuestion(
        question="What does filter(lambda x: x>0, [-1, 0, 1, 2]) produce when converted to list?",
        options=["[-1, 0, 1, 2]", "[0, 1, 2]", "[1, 2]", "Error"],
        correct_index=2,
        topic="Build-In Funcions",
        explanation="filter keeps only elements where the function returns True: 1 and 2."
    ),
    QuizQuestion(
        question="What does len([1, 2, 3]) return?",
        options=["3", "6", "1", "Error"],
        correct_index=0,
        topic="Build-In Funcions",
        explanation="len() returns the number of elements."
    ),
    QuizQuestion(
        question="What does reversed([1, 2, 3]) produce when converted to list?",
        options=["[1, 2, 3]", "[3, 2, 1]", "[3, 2, 1] as a copy", "Error"],
        correct_index=1,
        topic="Build-In Funcions",
        explanation="reversed() returns an iterator that yields elements in reverse order."
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
    QuizQuestion(
        question="What does class Child(Parent): mean?",
        options=["Child contains Parent", "Child inherits from Parent", "Child and Parent are the same", "Invalid syntax"],
        correct_index=1,
        topic="Classes",
        explanation="Child(Parent) means Child inherits from Parent."
    ),
    QuizQuestion(
        question="What does super() do?",
        options=["Calls the parent class's method", "Creates a super instance", "Imports a module", "Raises an error"],
        correct_index=0,
        topic="Classes",
        explanation="super() gives access to the parent class's methods."
    ),
    QuizQuestion(
        question="What is an instance attribute?",
        options=["Defined on the class", "Unique to each instance", "Shared by all instances", "Cannot be modified"],
        correct_index=1,
        topic="Classes",
        explanation="Instance attributes (e.g. self.x) belong to each object separately."
    ),
    QuizQuestion(
        question="What does @staticmethod do?",
        options=["Requires self", "Makes a method callable without instance", "Creates a class", "Is invalid in Python"],
        correct_index=1,
        topic="Classes",
        explanation="staticmethod allows calling the method without passing self."
    ),
    QuizQuestion(
        question="What does @classmethod receive as first argument?",
        options=["self", "cls (the class)", "Nothing", "The instance"],
        correct_index=1,
        topic="Classes",
        explanation="classmethod receives the class as the first argument (cls)."
    ),
    QuizQuestion(
        question="How do you create an instance of a class?",
        options=["new MyClass()", "MyClass()", "create MyClass()", "MyClass.new()"],
        correct_index=1,
        topic="Classes",
        explanation="Call the class like a function: obj = MyClass()."
    ),
    QuizQuestion(
        question="What does __repr__ define?",
        options=["User-friendly string", "Developer-friendly string representation", "Return value", "Constructor"],
        correct_index=1,
        topic="Classes",
        explanation="__repr__ should return an unambiguous representation for developers."
    ),
    QuizQuestion(
        question="Can a class inherit from multiple classes?",
        options=["No", "Yes, multiple inheritance is supported", "Only two classes", "Only with a special keyword"],
        correct_index=1,
        topic="Classes",
        explanation="class Child(A, B): inherits from both A and B."
    ),
    QuizQuestion(
        question="What does self refer to in a method?",
        options=["The class", "The current instance", "The parent class", "The module"],
        correct_index=1,
        topic="Classes",
        explanation="self is the instance the method is called on."
    ),
    QuizQuestion(
        question="What does __len__ define?",
        options=["The string representation", "The length returned by len()", "The constructor", "The destructor"],
        correct_index=1,
        topic="Classes",
        explanation="__len__ is called when len(obj) is used."
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
    QuizQuestion(
        question="What does file.read() return?",
        options=["One line", "The entire file as a string", "A list of lines", "The file object"],
        correct_index=1,
        topic="Files",
        explanation="read() reads and returns the entire file contents as a string."
    ),
    QuizQuestion(
        question="What does file.readlines() return?",
        options=["One line", "The whole file as string", "A list of lines", "A generator"],
        correct_index=2,
        topic="Files",
        explanation="readlines() returns a list of strings, one per line."
    ),
    QuizQuestion(
        question="What does 'with open(f) as f:' ensure?",
        options=["File is read faster", "File is closed when block exits", "File is locked", "File is deleted after"],
        correct_index=1,
        topic="Files",
        explanation="with ensures the file is closed when the block ends, even on errors."
    ),
    QuizQuestion(
        question="What does file.write('text') do?",
        options=["Reads text", "Writes text to the file", "Appends to a list", "Returns the file size"],
        correct_index=1,
        topic="Files",
        explanation="write() writes the string to the file (in write/append mode)."
    ),
    QuizQuestion(
        question="What mode creates a new file and fails if it exists?",
        options=["'w'", "'a'", "'x'", "'n'"],
        correct_index=2,
        topic="Files",
        explanation="'x' is exclusive creation - raises error if file exists."
    ),
    QuizQuestion(
        question="What does file.seek(0) do?",
        options=["Closes the file", "Moves to the start of the file", "Reads the first byte", "Deletes the file"],
        correct_index=1,
        topic="Files",
        explanation="seek(0) moves the file position to the beginning."
    ),
    QuizQuestion(
        question="What does 'b' in 'rb' mode mean?",
        options=["Big file", "Binary mode", "Buffer", "Backup"],
        correct_index=1,
        topic="Files",
        explanation="'b' opens the file in binary mode (bytes instead of text)."
    ),
    QuizQuestion(
        question="What does file.tell() return?",
        options=["The file name", "Current position in the file", "File size", "Number of lines"],
        correct_index=1,
        topic="Files",
        explanation="tell() returns the current byte position in the file."
    ),
    QuizQuestion(
        question="Which reads a file line by line efficiently?",
        options=["read()", "readlines()", "Iterating: for line in file", "readline() in a loop"],
        correct_index=2,
        topic="Files",
        explanation="for line in file iterates over lines without loading the whole file."
    ),
    QuizQuestion(
        question="What does 'w' mode do when opening a file?",
        options=["Read only", "Overwrites the file for writing", "Appends to the file", "Creates a backup"],
        correct_index=1,
        topic="Files",
        explanation="'w' opens for writing and truncates (overwrites) the file."
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
    QuizQuestion(
        question="What does Path('a/b/c').name return?",
        options=["'a/b'", "'c'", "'a'", "'a/b/c'"],
        correct_index=1,
        topic="loop through files",
        explanation=".name gives the final component (filename or directory name)."
    ),
    QuizQuestion(
        question="What does Path.mkdir(parents=True) do?",
        options=["Creates only the last directory", "Creates parent directories as needed", "Deletes the directory", "Moves the directory"],
        correct_index=1,
        topic="loop through files",
        explanation="parents=True creates any missing parent directories."
    ),
    QuizQuestion(
        question="What does os.path.exists(path) return?",
        options=["The file size", "True if path exists", "The file contents", "A list of files"],
        correct_index=1,
        topic="loop through files",
        explanation="exists() returns True if the path exists on the filesystem."
    ),
    QuizQuestion(
        question="What does Path.iterdir() return?",
        options=["File contents", "An iterator of entries in the directory", "A list of filenames", "The parent path"],
        correct_index=1,
        topic="loop through files",
        explanation="iterdir() yields Path objects for each entry in the directory."
    ),
    QuizQuestion(
        question="What does Path.parent give?",
        options=["The filename", "The parent directory path", "The file extension", "The full path"],
        correct_index=1,
        topic="loop through files",
        explanation=".parent returns the directory containing the path."
    ),
    QuizQuestion(
        question="How do you join paths with pathlib?",
        options=["path + '/' + name", "path / name", "path.join(name)", "os.path.join(path, name)"],
        correct_index=1,
        topic="loop through files",
        explanation="Path uses / operator: Path('a') / 'b' gives Path('a/b')."
    ),
    QuizQuestion(
        question="What does Path.is_file() return?",
        options=["True if it's a Python file", "True if path is a file (not directory)", "The file type", "Always False"],
        correct_index=1,
        topic="loop through files",
        explanation="is_file() returns True if the path exists and is a regular file."
    ),
    QuizQuestion(
        question="What does os.walk(path) yield?",
        options=["Filenames only", "(dirpath, dirnames, filenames) for each directory", "File contents", "A single path"],
        correct_index=1,
        topic="loop through files",
        explanation="walk() yields 3-tuples for each directory in the tree."
    ),
    QuizQuestion(
        question="What does Path.suffix return for 'data.csv'?",
        options=["'data'", "'.csv'", "'csv'", ""],
        correct_index=1,
        topic="loop through files",
        explanation=".suffix gives the file extension including the dot."
    ),
    QuizQuestion(
        question="Which creates a Path object?",
        options=["path('a/b')", "Path('a/b')", "Path = 'a/b'", "pathlib.path('a/b')"],
        correct_index=1,
        topic="loop through files",
        explanation="Path from pathlib: from pathlib import Path; Path('a/b')."
    ),
    QuizQuestion(
        question="What does Path.unlink() do?",
        options=["Creates a symlink", "Deletes the file", "Moves the file", "Copies the file"],
        correct_index=1,
        topic="loop through files",
        explanation="unlink() removes the file (deletes it)."
    ),
    QuizQuestion(
        question="What does Path.cwd() return?",
        options=["The home directory", "The current working directory", "The script directory", "The temp directory"],
        correct_index=1,
        topic="loop through files",
        explanation="cwd() returns the current working directory as a Path."
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
    QuizQuestion(
        question="What does plt.ylabel() set?",
        options=["The title", "The x-axis label", "The y-axis label", "The legend"],
        correct_index=2,
        topic="Matplotlib 1",
        explanation="ylabel() sets the label for the y-axis."
    ),
    QuizQuestion(
        question="What does plt.title() do?",
        options=["Sets axis labels", "Adds a title to the plot", "Creates a new figure", "Saves the figure"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="title() sets the main title of the plot."
    ),
    QuizQuestion(
        question="Which creates a scatter plot?",
        options=["plt.plot()", "plt.scatter()", "plt.point()", "plt.dot()"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="scatter(x, y) creates a scatter plot of points."
    ),
    QuizQuestion(
        question="What does plt.clf() do?",
        options=["Saves the figure", "Clears the current figure", "Closes the window", "Creates a new plot"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="clf() clears the current figure (removes all plots)."
    ),
    QuizQuestion(
        question="What does plt.savefig('out.png') do?",
        options=["Loads an image", "Saves the figure to a file", "Displays the figure", "Creates a new figure"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="savefig() saves the current figure to a file."
    ),
    QuizQuestion(
        question="What does plt.close() do?",
        options=["Saves and closes", "Closes the figure window", "Clears the axes", "Pauses the plot"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="close() closes the figure and frees memory."
    ),
    QuizQuestion(
        question="How do you set line color in plt.plot()?",
        options=["color='red'", "linecolor='red'", "set_color('red')", "plot(..., red)"],
        correct_index=0,
        topic="Matplotlib 1",
        explanation="color= or c= sets the line color: color='red' or c='r'."
    ),
    QuizQuestion(
        question="What does plt.grid(True) do?",
        options=["Creates a grid of subplots", "Adds grid lines to the axes", "Creates a table", "Nothing"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="grid(True) displays grid lines on the plot."
    ),
    QuizQuestion(
        question="What does plt.ylim(0, 10) do?",
        options=["Sets x-axis range", "Sets y-axis range to 0-10", "Creates 10 y-axes", "Sets the title"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="ylim(min, max) sets the y-axis limits."
    ),
    QuizQuestion(
        question="Which creates a histogram?",
        options=["plt.plot()", "plt.hist()", "plt.bar()", "plt.chart()"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="hist(data) creates a histogram of the data distribution."
    ),
    QuizQuestion(
        question="What does plt.xlim(0, 10) do?",
        options=["Sets y-axis range", "Sets x-axis range to 0-10", "Creates 10 subplots", "Sets the title"],
        correct_index=1,
        topic="Matplotlib 1",
        explanation="xlim(min, max) sets the x-axis limits."
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
    QuizQuestion(
        question="What does plt.tight_layout() do?",
        options=["Saves the figure", "Adjusts subplots to prevent overlap", "Creates a grid", "Closes the figure"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="tight_layout() adjusts spacing to prevent label overlap."
    ),
    QuizQuestion(
        question="What does plt.subplots(2, 2) return?",
        options=["A single axes", "(fig, axes_array)", "Four figures", "A list of figures"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="subplots(nrows, ncols) returns (figure, axes array)."
    ),
    QuizQuestion(
        question="How do you add a label to a line for the legend?",
        options=["label='My Line' in plot()", "legend_label='My Line'", "set_label('My Line')", "plot(..., 'My Line')"],
        correct_index=0,
        topic="Matplotlib 2",
        explanation="label='...' in plot() adds a label for the legend."
    ),
    QuizQuestion(
        question="What does axes.set_xlim(0, 5) do?",
        options=["Sets the title", "Sets x-axis limits to 0-5", "Creates 5 subplots", "Sets the figure size"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="set_xlim() sets the x-axis range for that axes."
    ),
    QuizQuestion(
        question="What does fig.add_subplot(2, 1, 1) do?",
        options=["Adds a title", "Adds the first subplot in a 2x1 grid", "Creates 2 figures", "Adds a legend"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="add_subplot(rows, cols, index) creates a subplot in the grid."
    ),
    QuizQuestion(
        question="What does plt.xticks(rotation=45) do?",
        options=["Rotates the figure", "Rotates x-axis labels 45 degrees", "Creates 45 ticks", "Rotates the plot"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="xticks(rotation=45) rotates x-axis tick labels."
    ),
    QuizQuestion(
        question="What does plt.suptitle() set?",
        options=["Subplot title", "Figure (overall) title", "Axis label", "Legend title"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="suptitle() sets the title for the entire figure."
    ),
    QuizQuestion(
        question="What does axes.get_xlim() return?",
        options=["The x-axis label", "(left, right) limits", "The number of ticks", "The figure"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="get_xlim() returns the current x-axis limits as (left, right)."
    ),
    QuizQuestion(
        question="What does plt.subplot(1, 2, 1) mean?",
        options=["1 row, 2 cols, select first", "2 rows, 1 col", "Create 2 figures", "Invalid"],
        correct_index=0,
        topic="Matplotlib 2",
        explanation="subplot(rows, cols, index) creates a grid and selects one."
    ),
    QuizQuestion(
        question="What does fig, ax = plt.subplots() return when no args?",
        options=["One figure, one axes", "Two figures", "One axes only", "Error"],
        correct_index=0,
        topic="Matplotlib 2",
        explanation="subplots() with no args creates one figure with one axes."
    ),
    QuizQuestion(
        question="What does plt.colorbar() add?",
        options=["A color legend", "A color scale bar", "Colored axes", "A new subplot"],
        correct_index=1,
        topic="Matplotlib 2",
        explanation="colorbar() adds a color scale (e.g. for heatmaps)."
    ),
    QuizQuestion(
        question="What does sharex=True do in plt.subplots?",
        options=["Shares the x-axis across subplots", "Creates shared figures", "Shares the title", "Nothing"],
        correct_index=0,
        topic="Matplotlib 2",
        explanation="sharex=True shares the x-axis between subplots."
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
    QuizQuestion(
        question="What does plt.text(x, y, s) require?",
        options=["Only s", "x, y, and s (coordinates and text)", "Only x and y", "A figure object"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="text(x, y, s) places string s at coordinates (x, y)."
    ),
    QuizQuestion(
        question="What does xy in plt.annotate() specify?",
        options=["The text position", "The point to point to", "The arrow color", "The font size"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="xy is the point the arrow points to."
    ),
    QuizQuestion(
        question="What does xytext in plt.annotate() specify?",
        options=["The point to point to", "Where the text is placed", "The arrow style", "The annotation color"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="xytext is where the text (and arrow end) is placed."
    ),
    QuizQuestion(
        question="What does fontsize=12 do in plt.text()?",
        options=["Sets the figure size", "Sets the text size to 12pt", "Sets 12 text boxes", "Nothing"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="fontsize=12 sets the text font size."
    ),
    QuizQuestion(
        question="What does ha='center' do in plt.text()?",
        options=["Sets the font", "Sets horizontal alignment", "Sets the color", "Sets the position"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="ha (horizontal alignment) can be 'left', 'center', 'right'."
    ),
    QuizQuestion(
        question="What does arrowprops do in plt.annotate()?",
        options=["Sets the text", "Configures the arrow (color, style)", "Sets the position", "Creates multiple arrows"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="arrowprops=dict(...) configures the arrow appearance."
    ),
    QuizQuestion(
        question="Can plt.text() be used without coordinates?",
        options=["Yes, it uses (0,0)", "No, x and y are required", "Only with subplots", "Only for titles"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="text(x, y, s) requires x and y for placement."
    ),
    QuizQuestion(
        question="What does va='top' do in plt.text()?",
        options=["Sets vertical alignment", "Sets the font", "Creates a title", "Sets the color"],
        correct_index=0,
        topic="Matplotlib Exercise - plt.text",
        explanation="va (vertical alignment) can be 'top', 'center', 'bottom'."
    ),
    QuizQuestion(
        question="What is the difference between text() and annotate()?",
        options=["No difference", "annotate() can add an arrow", "text() is deprecated", "annotate() is for titles only"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="annotate() can add an arrow from text to a point; text() is plain text only."
    ),
    QuizQuestion(
        question="What does bbox=dict(boxstyle='round') do in annotate?",
        options=["Creates a round figure", "Puts text in a rounded box", "Sets the arrow", "Creates a circle"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="bbox adds a box around the text; boxstyle='round' gives rounded corners."
    ),
    QuizQuestion(
        question="What does plt.text(0.5, 0.5, 'Hi') mean with axis limits 0-1?",
        options=["Places 'Hi' at center", "Places 'Hi' at top-right", "Invalid", "Places at bottom-left"],
        correct_index=0,
        topic="Matplotlib Exercise - plt.text",
        explanation="(0.5, 0.5) in data coordinates places text at the center."
    ),
    QuizQuestion(
        question="What does transform=ax.transAxes do in text()?",
        options=["Uses axes coordinates (0-1)", "Uses data coordinates", "Rotates the text", "Scales the figure"],
        correct_index=0,
        topic="Matplotlib Exercise - plt.text",
        explanation="transAxes uses relative coordinates (0,0)=bottom-left, (1,1)=top-right."
    ),
    QuizQuestion(
        question="What does fontweight='bold' do in plt.text()?",
        options=["Sets the color", "Makes the text bold", "Sets the size", "Sets the position"],
        correct_index=1,
        topic="Matplotlib Exercise - plt.text",
        explanation="fontweight='bold' makes the text bold."
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
    QuizQuestion(
        question="What does kind='line' do in df.plot()?",
        options=["Creates a bar chart", "Creates a line plot", "Creates a scatter plot", "Creates a table"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="kind='line' creates a line plot (default for DataFrame.plot())."
    ),
    QuizQuestion(
        question="What does kind='scatter' require in df.plot()?",
        options=["Nothing extra", "x and y column names", "A color column", "A size column"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="Scatter needs x= and y= to specify which columns to plot."
    ),
    QuizQuestion(
        question="What does df.plot(kind='pie') create?",
        options=["A bar chart", "A line plot", "A pie chart", "A scatter plot"],
        correct_index=2,
        topic="Pandas & Matplotlib",
        explanation="kind='pie' creates a pie chart from the data."
    ),
    QuizQuestion(
        question="What does ax=ax in df.plot(ax=ax) do?",
        options=["Creates a new axes", "Plots on the given axes", "Adds a title", "Saves the figure"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="ax=ax draws the plot on the specified axes object."
    ),
    QuizQuestion(
        question="What does df['col'].plot() plot?",
        options=["The whole DataFrame", "Only that column as a line", "A scatter plot", "Nothing"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="Series.plot() plots that column (index vs values)."
    ),
    QuizQuestion(
        question="What does kind='area' create?",
        options=["A bar chart", "An area chart (filled under line)", "A scatter plot", "A histogram"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="kind='area' creates an area chart with filled region under the line."
    ),
    QuizQuestion(
        question="What does df.plot(subplots=True) do?",
        options=["Creates one plot", "Creates separate subplot per column", "Creates a 3D plot", "Raises an error"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="subplots=True creates one subplot per column."
    ),
    QuizQuestion(
        question="What does df.plot.area() create?",
        options=["A bar chart", "A stacked area chart", "A scatter plot", "A pie chart"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="plot.area() creates a stacked area chart."
    ),
    QuizQuestion(
        question="What does df.plot(x='A', y='B') do?",
        options=["Plots A vs B", "Plots B vs A", "Plots both as separate lines", "Swaps columns"],
        correct_index=0,
        topic="Pandas & Matplotlib",
        explanation="x and y specify which columns to use for x and y axes."
    ),
    QuizQuestion(
        question="What does kind='box' create?",
        options=["A bar chart", "A box plot", "A line plot", "A scatter plot"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="kind='box' creates a box plot (box-and-whisker)."
    ),
    QuizQuestion(
        question="What does df.plot(legend=False) do?",
        options=["Adds a legend", "Hides the legend", "Creates a new figure", "Saves the plot"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="legend=False hides the legend."
    ),
    QuizQuestion(
        question="What does kind='hexbin' create?",
        options=["A bar chart", "A hexagonal binning plot", "A line plot", "A pie chart"],
        correct_index=1,
        topic="Pandas & Matplotlib",
        explanation="kind='hexbin' creates a hexagonal binning plot for 2D density."
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
    QuizQuestion(
        question="What does values= in pivot_table() specify?",
        options=["The index column", "The columns to aggregate", "The output format", "The row order"],
        correct_index=1,
        topic="Pandas 2",
        explanation="values= names the column(s) to aggregate."
    ),
    QuizQuestion(
        question="What does index= in pivot_table() specify?",
        options=["The columns to aggregate", "The row index (grouping)", "The column headers", "The fill value"],
        correct_index=1,
        topic="Pandas 2",
        explanation="index= specifies which column becomes the row index."
    ),
    QuizQuestion(
        question="What does columns= in pivot_table() specify?",
        options=["The row index", "The column headers (pivot dimension)", "The values to aggregate", "The fill value"],
        correct_index=1,
        topic="Pandas 2",
        explanation="columns= specifies which column becomes the column headers."
    ),
    QuizQuestion(
        question="What does aggfunc='mean' do in pivot_table?",
        options=["Counts rows", "Averages the values", "Sums the values", "Finds the max"],
        correct_index=1,
        topic="Pandas 2",
        explanation="aggfunc specifies the aggregation; 'mean' computes the average."
    ),
    QuizQuestion(
        question="What does df.groupby('col').size() return?",
        options=["The DataFrame length", "Count of rows per group", "The column size", "A Series of zeros"],
        correct_index=1,
        topic="Pandas 2",
        explanation="size() returns the number of rows in each group."
    ),
    QuizQuestion(
        question="What does df.groupby('col').count() return?",
        options=["Total count", "Non-null count per column per group", "The group keys", "A single number"],
        correct_index=1,
        topic="Pandas 2",
        explanation="count() returns the count of non-null values per column per group."
    ),
    QuizQuestion(
        question="What does .reset_index() do after groupby?",
        options=["Clears the index", "Moves the index back to columns", "Deletes the index", "Sorts by index"],
        correct_index=1,
        topic="Pandas 2",
        explanation="reset_index() converts the index back to regular columns."
    ),
    QuizQuestion(
        question="Can you groupby multiple columns?",
        options=["No", "Yes: df.groupby(['a','b'])", "Only with agg", "Only with pivot"],
        correct_index=1,
        topic="Pandas 2",
        explanation="groupby(['col1','col2']) groups by both columns."
    ),
    QuizQuestion(
        question="What does df.groupby('col').sum() return?",
        options=["A single number", "Sum per group per column", "The original DataFrame", "A list"],
        correct_index=1,
        topic="Pandas 2",
        explanation="sum() aggregates each numeric column by group."
    ),
    QuizQuestion(
        question="What does fill_value=0 do in pivot_table?",
        options=["Fills missing index", "Replaces NaN in result with 0", "Fills the index column", "Creates zeros"],
        correct_index=1,
        topic="Pandas 2",
        explanation="fill_value replaces NaN in the pivot result."
    ),
    QuizQuestion(
        question="What does margins=True do in pivot_table?",
        options=["Adds row/column totals", "Adds margins to the plot", "Creates a margin column", "Adds blank rows"],
        correct_index=0,
        topic="Pandas 2",
        explanation="margins=True adds All row and column for totals."
    ),
    QuizQuestion(
        question="What does df.groupby('col').mean() return?",
        options=["A single number", "Mean per group per numeric column", "The original DataFrame", "A list"],
        correct_index=1,
        topic="Pandas 2",
        explanation="mean() computes the average of each numeric column per group."
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
    QuizQuestion(
        question="What does how='inner' mean in merge()?",
        options=["Keep all rows from both", "Keep only matching rows", "Keep left rows only", "Keep right rows only"],
        correct_index=1,
        topic="Pandas 3",
        explanation="how='inner' keeps only rows with matching keys in both DataFrames."
    ),
    QuizQuestion(
        question="What does how='left' mean in merge()?",
        options=["Keep only matching", "Keep all from left, match from right", "Keep all from right", "Sort by left"],
        correct_index=1,
        topic="Pandas 3",
        explanation="how='left' keeps all rows from the left DataFrame, matching where possible."
    ),
    QuizQuestion(
        question="What does how='outer' mean in merge()?",
        options=["Keep only matching", "Keep all from both (union)", "Keep left only", "Keep right only"],
        correct_index=1,
        topic="Pandas 3",
        explanation="how='outer' keeps all rows from both (full outer join)."
    ),
    QuizQuestion(
        question="What does pd.concat([df1, df2], axis=1) do?",
        options=["Stacks vertically", "Stacks horizontally (side by side)", "Merges on a key", "Replaces df1"],
        correct_index=1,
        topic="Pandas 3",
        explanation="axis=1 concatenates along columns (horizontal)."
    ),
    QuizQuestion(
        question="What does join='inner' do in concat?",
        options=["Inner join on index", "Keeps only matching index rows", "Both A and B", "Nothing"],
        correct_index=2,
        topic="Pandas 3",
        explanation="join='inner' keeps only rows with matching index in all DataFrames."
    ),
    QuizQuestion(
        question="What does ignore_index=True do in concat?",
        options=["Ignores the index", "Resets index to 0,1,2,...", "Deletes the index", "Sorts by index"],
        correct_index=1,
        topic="Pandas 3",
        explanation="ignore_index=True creates a new default integer index."
    ),
    QuizQuestion(
        question="Can merge join on columns with different names?",
        options=["No", "Yes: left_on='a', right_on='b'", "Only with concat", "Only with join"],
        correct_index=1,
        topic="Pandas 3",
        explanation="left_on and right_on specify different column names for the join."
    ),
    QuizQuestion(
        question="What does suffixes=('_x','_y') do in merge?",
        options=["Adds prefixes", "Adds suffixes to duplicate column names", "Renames columns", "Deletes duplicates"],
        correct_index=1,
        topic="Pandas 3",
        explanation="suffixes rename overlapping columns (e.g. col_x, col_y)."
    ),
    QuizQuestion(
        question="What does df1.join(df2) do?",
        options=["Joins on index by default", "Always joins on columns", "Concatenates vertically", "Replaces df1"],
        correct_index=0,
        topic="Pandas 3",
        explanation="join() merges on index by default (like SQL join)."
    ),
    QuizQuestion(
        question="What does pd.merge(df1, df2, on='key') require?",
        options=["Both have 'key' column", "Only df1 has 'key'", "Only df2 has 'key'", "Neither has 'key'"],
        correct_index=0,
        topic="Pandas 3",
        explanation="on='key' requires both DataFrames to have a 'key' column."
    ),
    QuizQuestion(
        question="What does concat with keys=['A','B'] do?",
        options=["Renames columns", "Adds a level to the index identifying source", "Deletes rows", "Sorts the result"],
        correct_index=1,
        topic="Pandas 3",
        explanation="keys= adds a level to the index to identify which DataFrame each row came from."
    ),
    QuizQuestion(
        question="What does how='right' mean in merge()?",
        options=["Keep only matching", "Keep all from left", "Keep all from right, match from left", "Sort by right"],
        correct_index=2,
        topic="Pandas 3",
        explanation="how='right' keeps all rows from the right DataFrame."
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
    QuizQuestion(
        question="What does bool('') return?",
        options=["True", "False", "''", "Error"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="Empty string is falsy; bool('') is False."
    ),
    QuizQuestion(
        question="What does float(3) return?",
        options=["3", "3.0", "'3.0'", "Error"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="float() converts to float: float(3) = 3.0."
    ),
    QuizQuestion(
        question="What is type([])?",
        options=["tuple", "list", "dict", "set"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="[] creates a list."
    ),
    QuizQuestion(
        question="What does 'hello'.replace('l','L') return?",
        options=["'hello'", "'heLLo'", "'heLLo' (new string)", "'HELLO'"],
        correct_index=2,
        topic="Variables & DataTypes",
        explanation="replace() returns a new string with replacements (strings are immutable)."
    ),
    QuizQuestion(
        question="What does '  hi  '.strip() return?",
        options=["'  hi  '", "'hi'", "' hi '", "Error"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="strip() removes leading and trailing whitespace."
    ),
    QuizQuestion(
        question="What does 'a' in 'abc' return?",
        options=["True", "False", "0", "1"],
        correct_index=0,
        topic="Variables & DataTypes",
        explanation="'in' checks substring membership: 'a' in 'abc' is True."
    ),
    QuizQuestion(
        question="What does [1, 2] * 2 produce?",
        options=["[2, 4]", "[1, 2, 1, 2]", "[1, 2, 2]", "Error"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="list * n repeats the list n times."
    ),
    QuizQuestion(
        question="What does bool([]) return?",
        options=["True", "False", "0", "None"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="Empty list is falsy; bool([]) is False."
    ),
    QuizQuestion(
        question="What does bool([0]) return?",
        options=["True", "False", "0", "None"],
        correct_index=0,
        topic="Variables & DataTypes",
        explanation="Non-empty list is truthy; bool([0]) is True (the list has one element)."
    ),
    QuizQuestion(
        question="What does 'hi'.split() return?",
        options=["['h','i']", "['hi']", "['hi'] (splits on whitespace)", "Error"],
        correct_index=2,
        topic="Variables & DataTypes",
        explanation="split() with no arg splits on whitespace: 'hi'.split() = ['hi']."
    ),
    QuizQuestion(
        question="What does ','.join(['a','b','c']) return?",
        options=["'a,b,c'", "['a','b','c']", "'abc'", "Error"],
        correct_index=0,
        topic="Variables & DataTypes",
        explanation="join() concatenates strings with the separator: 'a'+','+'b'+','+'c'."
    ),
    QuizQuestion(
        question="What does isinstance(5, int) return?",
        options=["True", "False", "5", "int"],
        correct_index=0,
        topic="Variables & DataTypes",
        explanation="isinstance(obj, type) checks if obj is of that type."
    ),
    QuizQuestion(
        question="What does hex(255) return?",
        options=["'255'", "'0xff'", "255", "Error"],
        correct_index=1,
        topic="Variables & DataTypes",
        explanation="hex() converts an int to a hexadecimal string."
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
