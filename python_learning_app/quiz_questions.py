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
    QuizQuestion(question="What does 'abc'.capitalize() return?", options=["'Abc'", "'ABC'", "'abc'", "Error"], correct_index=0, topic="Variables & Data Types", explanation="capitalize() makes the first character uppercase."),
    QuizQuestion(question="What is 3 + 4 * 2?", options=["14", "11", "10", "Error"], correct_index=1, topic="Variables & Data Types", explanation="* has higher precedence: 4*2=8, then 3+8=11."),
    QuizQuestion(question="What does 'test'.startswith('te') return?", options=["True", "False", "0", "1"], correct_index=0, topic="Variables & Data Types", explanation="startswith() returns True if string starts with the prefix."),
    QuizQuestion(question="What does 'test'.endswith('st') return?", options=["True", "False", "0", "1"], correct_index=0, topic="Variables & Data Types", explanation="endswith() returns True if string ends with the suffix."),
    QuizQuestion(question="What is (1, 2) + (3, 4)?", options=["(1, 2, 3, 4)", "(4, 6)", "Error", "(1, 3, 2, 4)"], correct_index=0, topic="Variables & Data Types", explanation="+ concatenates tuples."),
    QuizQuestion(question="What does '  spaces  '.strip() return?", options=["'  spaces  '", "'spaces'", "'spaces  '", "'  spaces'"], correct_index=1, topic="Variables & Data Types", explanation="strip() removes leading and trailing whitespace."),
    QuizQuestion(question="What is 1.5 + 1.5?", options=["2", "3.0", "2.0", "3"], correct_index=2, topic="Variables & Data Types", explanation="Float addition: 1.5 + 1.5 = 3.0."),
    QuizQuestion(question="What does 'hi' * 3 return?", options=["'hihihi'", "'hi hi hi'", "Error", "6"], correct_index=0, topic="Variables & Data Types", explanation="String * n repeats the string n times."),
    QuizQuestion(question="What does 'hello'.find('l') return?", options=["2", "3", "2 (first occurrence)", "-1"], correct_index=2, topic="Variables & Data Types", explanation="find() returns the index of the first occurrence (2)."),
    QuizQuestion(question="What does 'hello'.count('l') return?", options=["1", "2", "3", "0"], correct_index=1, topic="Variables & Data Types", explanation="count() returns how many times the substring appears."),
    QuizQuestion(question="What is type(3.14)?", options=["int", "float", "double", "decimal"], correct_index=1, topic="Variables & Data Types", explanation="Numbers with decimals are float."),
    QuizQuestion(question="What does 'a' not in 'abc' return?", options=["True", "False", "Error", "None"], correct_index=1, topic="Variables & Data Types", explanation="'a' is in 'abc', so 'not in' returns False."),
    QuizQuestion(question="What is -5 // 2?", options=["-2", "-3", "-2.5", "2"], correct_index=1, topic="Variables & Data Types", explanation="Floor division rounds toward negative infinity: -3."),
    QuizQuestion(question="What does round(2.5) return?", options=["2", "3", "2.5", "2.0"], correct_index=0, topic="Variables & Data Types", explanation="round() uses banker's rounding: 2.5 rounds to 2."),
    QuizQuestion(question="What does 'Hi'.swapcase() return?", options=["'hi'", "'HI'", "'hI'", "Error"], correct_index=2, topic="Variables & Data Types", explanation="swapcase() swaps upper/lower: H→h, i→I."),
    QuizQuestion(question="What is 0 or 5?", options=["0", "5", "True", "False"], correct_index=1, topic="Variables & Data Types", explanation="or returns the first truthy value; 5 is truthy."),
    QuizQuestion(question="What is 1 and 0?", options=["1", "0", "True", "False"], correct_index=1, topic="Variables & Data Types", explanation="and returns the first falsy value or the last; 0 is falsy."),
    QuizQuestion(question="What does 'abc'[::2] return?", options=["'ac'", "'ab'", "'abc'", "'b'"], correct_index=0, topic="Variables & Data Types", explanation="[::2] takes every 2nd character: a, c."),
    QuizQuestion(question="What does 'abc'[::-1] return?", options=["'cba'", "'abc'", "'a'", "Error"], correct_index=0, topic="Variables & Data Types", explanation="[::-1] reverses the string."),
    QuizQuestion(question="What is 2 in [1, 2, 3]?", options=["True", "False", "1", "2"], correct_index=0, topic="Variables & Data Types", explanation="in checks membership in a list."),
    QuizQuestion(question="What does 'test'.isalpha() return for 'test'?", options=["True", "False", "4", "Error"], correct_index=0, topic="Variables & Data Types", explanation="isalpha() returns True if all chars are letters."),
    QuizQuestion(question="What does '123'.isdigit() return?", options=["True", "False", "123", "3"], correct_index=0, topic="Variables & Data Types", explanation="isdigit() returns True if all chars are digits."),
    QuizQuestion(question="What is 3 < 5 < 7?", options=["True", "False", "5", "Error"], correct_index=0, topic="Variables & Data Types", explanation="Chained comparison: 3<5 and 5<7."),
    QuizQuestion(question="What does 'hello'.index('e') return?", options=["1", "2", "0", "Error"], correct_index=0, topic="Variables & Data Types", explanation="index() returns the position of the substring."),
    QuizQuestion(question="What is 3 + 4.0?", options=["7", "7.0", "Error", "12"], correct_index=1, topic="Variables & Data Types", explanation="int + float promotes to float: 7.0."),
    QuizQuestion(question="What does 'hi'.center(6) return?", options=["'  hi  '", "'hi'", "' hi '", "Error"], correct_index=0, topic="Variables & Data Types", explanation="center() pads to width 6 with spaces."),
    QuizQuestion(question="What is 3 != 3?", options=["True", "False", "0", "1"], correct_index=1, topic="Variables & Data Types", explanation="!= is not equal; 3 equals 3."),
    QuizQuestion(question="What does '  hi  '.lstrip() return?", options=["'  hi  '", "'hi  '", "'  hi'", "'hi'"], correct_index=1, topic="Variables & Data Types", explanation="lstrip() removes leading whitespace only."),
    QuizQuestion(question="What does '  hi  '.rstrip() return?", options=["'  hi  '", "'hi  '", "'  hi'", "'hi'"], correct_index=2, topic="Variables & Data Types", explanation="rstrip() removes trailing whitespace only."),
    QuizQuestion(question="What is 2.0 == 2?", options=["True", "False", "Error", "None"], correct_index=0, topic="Variables & Data Types", explanation="2.0 and 2 are equal in value."),
    QuizQuestion(question="What does 'a'.join(['x','y','z']) return?", options=["'xayaz'", "'xyz'", "'a'", "Error"], correct_index=0, topic="Variables & Data Types", explanation="join() puts the separator between elements."),
    QuizQuestion(question="What is not True?", options=["True", "False", "None", "0"], correct_index=1, topic="Variables & Data Types", explanation="not True is False."),
    QuizQuestion(question="What does 'hello'.replace('l','',1) return?", options=["'heo'", "'hello'", "'helo'", "Error"], correct_index=2, topic="Variables & Data Types", explanation="Replace first 1 occurrence: first 'l'→''."),
    QuizQuestion(question="What is 1 == 1.0?", options=["True", "False", "Error", "None"], correct_index=0, topic="Variables & Data Types", explanation="== compares values; 1 and 1.0 are equal."),
    QuizQuestion(question="What does 'test'.split('e') return?", options=["['t','st']", "['test']", "['t','e','s','t']", "Error"], correct_index=0, topic="Variables & Data Types", explanation="split('e') splits on 'e': 't' + 'st'."),
    QuizQuestion(question="What is 3 * 'ab'?", options=["'ababab'", "'ab'", "Error", "6"], correct_index=0, topic="Variables & Data Types", explanation="String * n repeats: 'ab'*3 = 'ababab'."),
    QuizQuestion(question="What does 'HI'.isupper() return?", options=["True", "False", "2", "Error"], correct_index=0, topic="Variables & Data Types", explanation="isupper() returns True if all letters are uppercase."),
    QuizQuestion(question="What is 3 > 4?", options=["True", "False", "0", "1"], correct_index=1, topic="Variables & Data Types", explanation="3 is not greater than 4."),
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
    QuizQuestion(question="What does for _ in range(3): pass do?", options=["Nothing, loops 3 times", "Raises error", "Runs once", "Skips 3 times"], correct_index=0, topic="Control Flow", explanation="_ is a throwaway variable; loop runs 3 times."),
    QuizQuestion(question="What is the output? i=0; while i<2: i+=1; print(i)", options=["1, 2", "0, 1", "1, 2, 3", "0, 1, 2"], correct_index=0, topic="Control Flow", explanation="i goes 0→1 (print 1), 1→2 (print 2), then 2<2 is False."),
    QuizQuestion(question="What does else in while loop do?", options=["Runs if loop was broken", "Runs if loop completes normally", "Runs every iteration", "Invalid syntax"], correct_index=1, topic="Control Flow", explanation="while-else runs else block if loop completes without break."),
    QuizQuestion(question="What is for i in range(0): print(i)?", options=["Prints nothing", "Prints 0", "Error", "Infinite loop"], correct_index=0, topic="Control Flow", explanation="range(0) is empty; loop body never runs."),
    QuizQuestion(question="What does if x: mean when x=0?", options=["True branch runs", "False branch runs", "Error", "Neither runs"], correct_index=1, topic="Control Flow", explanation="0 is falsy; the else/False branch runs."),
    QuizQuestion(question="What does if x: mean when x=''?", options=["True branch runs", "False branch runs", "Error", "Neither runs"], correct_index=1, topic="Control Flow", explanation="Empty string is falsy."),
    QuizQuestion(question="What is range(5)[2]?", options=["2", "3", "5", "Error"], correct_index=0, topic="Control Flow", explanation="range(5) is indexable; index 2 gives 2."),
    QuizQuestion(question="What does for i in range(1,4): print(i) output?", options=["1, 2, 3", "1, 2, 3, 4", "0, 1, 2, 3", "2, 3, 4"], correct_index=0, topic="Control Flow", explanation="range(1,4) yields 1, 2, 3."),
    QuizQuestion(question="What happens with while True: break?", options=["Infinite loop", "Runs once then exits", "Error", "Never runs"], correct_index=1, topic="Control Flow", explanation="break exits immediately on first iteration."),
    QuizQuestion(question="What does for i in range(3): continue; print(i) do?", options=["Prints 0,1,2", "Prints nothing", "Error", "Prints 3"], correct_index=1, topic="Control Flow", explanation="continue skips print; it runs before continue, but continue skips rest."),
    QuizQuestion(question="What is the output? x=1; print(x) if x else print(0)", options=["1", "0", "Error", "None"], correct_index=0, topic="Control Flow", explanation="x is truthy, so print(x) runs, outputs 1."),
    QuizQuestion(question="What does if not []: mean?", options=["True branch", "False branch", "Error", "Neither"], correct_index=0, topic="Control Flow", explanation="not [] is not False = True; empty list is falsy."),
    QuizQuestion(question="What is 5 if True else 10?", options=["5", "10", "True", "Error"], correct_index=0, topic="Control Flow", explanation="Ternary: True branch returns 5."),
    QuizQuestion(question="What is 5 if False else 10?", options=["5", "10", "False", "Error"], correct_index=1, topic="Control Flow", explanation="Ternary: False branch returns 10."),
    QuizQuestion(question="What does for i in reversed(range(3)): print(i) output?", options=["2, 1, 0", "0, 1, 2", "3, 2, 1", "Error"], correct_index=0, topic="Control Flow", explanation="reversed(range(3)) yields 2, 1, 0."),
    QuizQuestion(question="What is the output? for i in range(2): pass; print('done')", options=["'done' once", "'done' twice", "Nothing", "Error"], correct_index=0, topic="Control Flow", explanation="Loop runs 2 times (pass), then print runs once."),
    QuizQuestion(question="What does if 1: print('ok') do?", options=["Prints 'ok'", "Prints nothing", "Error", "Prints 1"], correct_index=0, topic="Control Flow", explanation="1 is truthy; the if block runs."),
    QuizQuestion(question="What does if 0: print('ok') else: print('no') do?", options=["Prints 'ok'", "Prints 'no'", "Error", "Prints nothing"], correct_index=1, topic="Control Flow", explanation="0 is falsy; else block runs."),
    QuizQuestion(question="What is for i in (1,2,3): print(i)?", options=["1, 2, 3", "0, 1, 2", "Error", "(1,2,3)"], correct_index=0, topic="Control Flow", explanation="for iterates over tuple elements."),
    QuizQuestion(question="What does break outside a loop do?", options=["Exits the script", "Raises SyntaxError", "Does nothing", "Exits the function"], correct_index=1, topic="Control Flow", explanation="break/continue must be inside a loop."),
    QuizQuestion(question="What does for i in 'ab': print(i) output?", options=["a, b", "ab", "0, 1", "Error"], correct_index=0, topic="Control Flow", explanation="for over string iterates over characters."),
    QuizQuestion(question="What is while False: pass?", options=["Runs forever", "Runs once", "Never runs", "Error"], correct_index=2, topic="Control Flow", explanation="Condition is False; loop body never executes."),
    QuizQuestion(question="What does range(10)[-1] return?", options=["9", "10", "0", "Error"], correct_index=0, topic="Control Flow", explanation="range(10) is 0..9; -1 is last element, 9."),
    QuizQuestion(question="What is for i in range(2): break?", options=["Loops twice", "Runs once then exits", "Error", "Never runs"], correct_index=1, topic="Control Flow", explanation="First iteration hits break, exits."),
    QuizQuestion(question="What does if x in [1,2,3]: mean when x=2?", options=["True branch", "False branch", "Error", "Neither"], correct_index=0, topic="Control Flow", explanation="2 is in the list; condition is True."),
    QuizQuestion(question="What does elif do?", options=["Same as else", "Else-if: check another condition", "End the if", "Invalid keyword"], correct_index=1, topic="Control Flow", explanation="elif checks another condition if previous failed."),
    QuizQuestion(question="What is the output? for i in range(1): print(i)", options=["0", "1", "Nothing", "Error"], correct_index=0, topic="Control Flow", explanation="range(1) yields 0; loop runs once."),
    QuizQuestion(question="What does for i in range(3): if i==1: continue; print(i) output?", options=["0, 2", "0, 1, 2", "1", "Error"], correct_index=0, topic="Control Flow", explanation="When i=1, continue skips print; 0 and 2 print."),
    QuizQuestion(question="What is if 1: x=5 else: x=10?", options=["x=5", "x=10", "Error", "x=1"], correct_index=0, topic="Control Flow", explanation="1 is truthy; x gets 5."),
    QuizQuestion(question="What does while 1: break do?", options=["Infinite loop", "Runs once, exits", "Error", "Never runs"], correct_index=1, topic="Control Flow", explanation="Enters loop, break exits immediately."),
    QuizQuestion(question="What is for i in range(2,2): print(i)?", options=["Prints nothing", "Prints 2", "Error", "Prints 0,1"], correct_index=0, topic="Control Flow", explanation="range(2,2) is empty (start equals stop)."),
    QuizQuestion(question="What does if None: print('x') else: print('y') do?", options=["Prints 'x'", "Prints 'y'", "Error", "Prints nothing"], correct_index=1, topic="Control Flow", explanation="None is falsy; else runs."),
    QuizQuestion(question="What is x=3; 'big' if x>2 else 'small'?", options=["'big'", "'small'", "3", "True"], correct_index=0, topic="Control Flow", explanation="x>2 is True; ternary returns 'big'."),
    QuizQuestion(question="What does for i in range(0,5,2): print(i) output?", options=["0, 2, 4", "0, 2", "2, 4", "0, 1, 2, 3, 4"], correct_index=0, topic="Control Flow", explanation="range(0,5,2) yields 0, 2, 4."),
    QuizQuestion(question="What is the output? a,b=1,2; print(a if a>b else b)", options=["1", "2", "Error", "None"], correct_index=1, topic="Control Flow", explanation="a>b is False; else returns b=2."),
    QuizQuestion(question="What does if []: ... else: ... do?", options=["Runs if block", "Runs else block", "Error", "Runs both"], correct_index=1, topic="Control Flow", explanation="[] is falsy; else block runs."),
    QuizQuestion(question="What is for x in range(3): x+=1; print(x)?", options=["1, 2, 3", "0, 1, 2", "1, 2, 3, 4", "Error"], correct_index=0, topic="Control Flow", explanation="x is 0,1,2; x+=1 gives 1,2,3; prints those."),
    QuizQuestion(question="What does if '': print('a') else: print('b') do?", options=["Prints 'a'", "Prints 'b'", "Error", "Prints nothing"], correct_index=1, topic="Control Flow", explanation="Empty string is falsy; else runs."),
    QuizQuestion(question="What is range(3)[1:3]?", options=["range(1, 3)", "1, 2", "[1, 2]", "Error"], correct_index=0, topic="Control Flow", explanation="Slicing range returns a range object."),
    QuizQuestion(question="What does for i in range(2): pass; print(i) output?", options=["1", "0, 1", "Error", "2"], correct_index=0, topic="Control Flow", explanation="After loop, i is last value (1); print runs once."),
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
    QuizQuestion(question="What does def f(x, y=10): mean?", options=["y is required", "y defaults to 10 if not provided", "Invalid syntax", "y must be 10"], correct_index=1, topic="Functions", explanation="y=10 gives a default; callers can omit it."),
    QuizQuestion(question="What does def f(*args): return len(args) do for f(1,2,3)?", options=["3", "1", "Error", "6"], correct_index=0, topic="Functions", explanation="*args collects (1,2,3); len is 3."),
    QuizQuestion(question="What does def f(**kwargs): return kwargs do for f(a=1,b=2)?", options=["{'a':1,'b':2}", "1, 2", "Error", "(1,2)"], correct_index=0, topic="Functions", explanation="**kwargs collects keyword args into a dict."),
    QuizQuestion(question="Can you have *args and **kwargs in the same function?", options=["No", "Yes, args before kwargs", "Only in built-ins", "Only with default args"], correct_index=1, topic="Functions", explanation="def f(*args, **kwargs) is valid; * before **."),
    QuizQuestion(question="What does a closure capture?", options=["Nothing", "Variables from enclosing scope", "Only globals", "Only parameters"], correct_index=1, topic="Functions", explanation="Closure captures variables from the enclosing function."),
    QuizQuestion(question="What is def f(): return 1, 2?", options=["Returns tuple (1, 2)", "Returns 1 only", "Error", "Returns 1 and 2 separately"], correct_index=0, topic="Functions", explanation="return 1, 2 returns a tuple (1, 2)."),
    QuizQuestion(question="What does f.__name__ give?", options=["The return value", "The function's name as string", "The module name", "Error"], correct_index=1, topic="Functions", explanation="__name__ is the function's name attribute."),
    QuizQuestion(question="What does def f(x): x.append(1) do to a list passed in?", options=["Creates a copy", "Modifies the original list", "Returns a new list", "Raises error"], correct_index=1, topic="Functions", explanation="Lists are mutable; append modifies in place."),
    QuizQuestion(question="What is the output of def f(): return; print(1)?", options=["1", "None", "Error", "Nothing prints"], correct_index=3, topic="Functions", explanation="return exits before print; nothing prints."),
    QuizQuestion(question="What does def f(x=[]): x.append(1); return x do on second call f()?", options=["[1]", "[1, 1]", "Error", "[]"], correct_index=1, topic="Functions", explanation="Mutable default is shared; second call gets [1,1]."),
    QuizQuestion(question="What does lambda x: x*2 do?", options=["Multiplies x by 2", "Returns a function", "Both", "Error"], correct_index=2, topic="Functions", explanation="lambda creates a function that returns x*2."),
    QuizQuestion(question="What does map(f, [1,2,3]) return?", options=["A list", "A map object (iterator)", "1, 2, 3", "Error"], correct_index=1, topic="Functions", explanation="map() returns an iterator, not a list."),
    QuizQuestion(question="What does filter(None, [0,1,2]) produce when converted to list?", options=["[0,1,2]", "[1, 2]", "[0]", "Error"], correct_index=1, topic="Functions", explanation="None as predicate filters out falsy values."),
    QuizQuestion(question="What does sorted([3,1,2], reverse=True) return?", options=["[1,2,3]", "[3,2,1]", "Error", "[2,1,3]"], correct_index=1, topic="Functions", explanation="reverse=True sorts descending."),
    QuizQuestion(question="What does def f(): yield 1; yield 2 create?", options=["A list", "A generator", "A tuple", "Error"], correct_index=1, topic="Functions", explanation="yield makes it a generator function."),
    QuizQuestion(question="What does next(g) do for generator g?", options=["Runs until return", "Gets next yielded value", "Raises always", "Resets generator"], correct_index=1, topic="Functions", explanation="next() advances the generator and returns the next value."),
    QuizQuestion(question="What does def f(a, b, *, c): mean?", options=["c is optional", "c must be keyword-only", "Invalid syntax", "c has default"], correct_index=1, topic="Functions", explanation="* forces c to be passed as keyword."),
    QuizQuestion(question="What does functools.partial(f, 1) do?", options=["Calls f(1)", "Creates a new function with first arg fixed as 1", "Raises error", "Returns 1"], correct_index=1, topic="Functions", explanation="partial fixes arguments; returns a callable."),
    QuizQuestion(question="What does def f(): global x; x=5 do?", options=["Creates local x", "Modifies module-level x", "Error", "Does nothing"], correct_index=1, topic="Functions", explanation="global x allows assigning to the global variable."),
    QuizQuestion(question="What is (lambda x,y: x+y)(2,3)?", options=["5", "6", "Error", "23"], correct_index=0, topic="Functions", explanation="Lambda adds 2 and 3, returns 5."),
    QuizQuestion(question="What does def f(): return yield 1 do?", options=["Returns 1", "Creates generator", "Error", "Returns None"], correct_index=2, topic="Functions", explanation="return and yield cannot be in same function."),
    QuizQuestion(question="What does def f(x): return x*2; g=f; g(3) return?", options=["6", "3", "Error", "None"], correct_index=0, topic="Functions", explanation="g references f; g(3) calls f(3)=6."),
    QuizQuestion(question="What does def f(a, b=2, c=3): pass allow?", options=["f(1)", "f(1, 2)", "f(1, c=5)", "All of the above"], correct_index=3, topic="Functions", explanation="All are valid: a=1; or a=1,b=2; or a=1,c=5."),
    QuizQuestion(question="What does nonlocal x do?", options=["Creates global x", "Refers to x in enclosing scope", "Creates local x", "Imports x"], correct_index=1, topic="Functions", explanation="nonlocal allows modifying variable from enclosing function."),
    QuizQuestion(question="What does def f(): return; 1+1 do?", options=["Returns 2", "Returns None", "Error", "Runs 1+1 then returns"], correct_index=1, topic="Functions", explanation="return exits immediately; 1+1 never runs."),
    QuizQuestion(question="What is max(1, 2, 3)?", options=["3", "6", "1", "Error"], correct_index=0, topic="Functions", explanation="max() returns the largest argument."),
    QuizQuestion(question="What does def f(a, *args, b): mean?", options=["b is keyword-only", "Invalid", "b has default", "args before b"], correct_index=0, topic="Functions", explanation="After *args, b must be passed by keyword."),
    QuizQuestion(question="What does list(generator) do?", options=["Nothing", "Consumes generator into list", "Error", "Returns empty"], correct_index=1, topic="Functions", explanation="list() consumes the iterator into a list."),
    QuizQuestion(question="What does def f(): x=1; def g(): return x; return g create?", options=["Returns 1", "Returns function g (closure)", "Error", "Returns x"], correct_index=1, topic="Functions", explanation="g captures x from f; returning g returns the closure."),
    QuizQuestion(question="What does def f(a, b, /, c): mean?", options=["a,b positional-only", "c keyword-only", "Invalid", "a,b keyword-only"], correct_index=0, topic="Functions", explanation="/ means a and b must be positional."),
    QuizQuestion(question="What does help(f) show?", options=["Nothing", "Docstring and signature", "Source code", "Return value"], correct_index=1, topic="Functions", explanation="help() displays the docstring and signature."),
    QuizQuestion(question="What does def f(): return 1; return 2 return?", options=["1", "2", "Error", "None"], correct_index=0, topic="Functions", explanation="First return exits; second never runs."),
    QuizQuestion(question="What does callable(x) return for a function?", options=["False", "True", "Error", "The function"], correct_index=1, topic="Functions", explanation="callable() returns True for functions."),
    QuizQuestion(question="What does def f(x, y): return x+y; f(1) do?", options=["Returns 1", "TypeError", "Returns 2", "Error"], correct_index=1, topic="Functions", explanation="Missing required argument y; TypeError."),
    QuizQuestion(question="What does getattr(obj, 'meth') return?", options=["The method", "Calling it", "Error", "None"], correct_index=0, topic="Functions", explanation="getattr retrieves the attribute by name."),
    QuizQuestion(question="What does def f(): pass; type(f) return?", options=["function", "None", "type", "Error"], correct_index=0, topic="Functions", explanation="type(f) is function (or types.FunctionType)."),
    QuizQuestion(question="What does def f(a, b, c=0): pass; f(1, 2, 3) do?", options=["a=1,b=2,c=3", "a=1,b=2,c=0", "Error", "a=1,b=2"], correct_index=0, topic="Functions", explanation="Third arg 3 overrides default c=0."),
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
    QuizQuestion(question="What does [1,2,3].remove(2) do?", options=["Returns 2", "Removes 2 in place, returns None", "Error", "Removes index 2"], correct_index=1, topic="Data Structures", explanation="remove() deletes first occurrence of value."),
    QuizQuestion(question="What does [1,2,3].clear() do?", options=["Returns []", "Removes all elements in place", "Error", "Returns None"], correct_index=1, topic="Data Structures", explanation="clear() removes all elements; list becomes []."),
    QuizQuestion(question="What does [1,2,2,3].count(2) return?", options=["1", "2", "3", "0"], correct_index=1, topic="Data Structures", explanation="count() returns how many times the value appears."),
    QuizQuestion(question="What does [1,2,3].index(2) return?", options=["1", "2", "0", "Error"], correct_index=0, topic="Data Structures", explanation="index() returns the position of the value."),
    QuizQuestion(question="What does [3,1,2].sort() return?", options=["[1,2,3]", "None", "Error", "Sorted copy"], correct_index=1, topic="Data Structures", explanation="sort() sorts in place, returns None."),
    QuizQuestion(question="What does sorted([3,1,2]) return?", options=["[1,2,3]", "None", "Error", "Sorted in place"], correct_index=0, topic="Data Structures", explanation="sorted() returns a new sorted list."),
    QuizQuestion(question="What does [1,2,3].reverse() do?", options=["Returns reversed list", "Reverses in place, returns None", "Error", "Returns [3,2,1]"], correct_index=1, topic="Data Structures", explanation="reverse() reverses in place."),
    QuizQuestion(question="What does [1,2,3].copy() return?", options=["Same list", "Shallow copy (new list)", "Error", "Deep copy"], correct_index=1, topic="Data Structures", explanation="copy() creates a shallow copy."),
    QuizQuestion(question="What does 'a' in {'a':1} return?", options=["True", "False", "1", "Error"], correct_index=0, topic="Data Structures", explanation="'in' checks keys; 'a' is a key."),
    QuizQuestion(question="What does d.pop('a') do?", options=["Removes and returns value for 'a'", "Removes 'a' only", "Error if missing", "Both A and C"], correct_index=3, topic="Data Structures", explanation="pop() removes and returns; KeyError if missing (unless default given)."),
    QuizQuestion(question="What does d.pop('x', 0) do when 'x' missing?", options=["KeyError", "Returns 0", "Returns None", "Adds 'x':0"], correct_index=1, topic="Data Structures", explanation="Second arg is default when key missing."),
    QuizQuestion(question="What does {1,2} | {2,3} return?", options=["{1,2,3}", "{2}", "Error", "[1,2,3]"], correct_index=0, topic="Data Structures", explanation="| is set union."),
    QuizQuestion(question="What does {1,2} & {2,3} return?", options=["{1,2,3}", "{2}", "Error", "[]"], correct_index=1, topic="Data Structures", explanation="& is set intersection."),
    QuizQuestion(question="What does {1,2} - {2,3} return?", options=["{1}", "{1,3}", "Error", "{-1}"], correct_index=0, topic="Data Structures", explanation="- is set difference; elements in first not in second."),
    QuizQuestion(question="What does dict.fromkeys(['a','b'], 0) create?", options=["{'a':0,'b':0}", "['a','b']", "Error", "{}"], correct_index=0, topic="Data Structures", explanation="fromkeys creates dict with keys and same value."),
    QuizQuestion(question="What does [1,2]+[3,4] produce?", options=["[1,2,3,4]", "[4,6]", "Error", "[1,3,2,4]"], correct_index=0, topic="Data Structures", explanation="+ concatenates lists."),
    QuizQuestion(question="What does (1,2)[0] = 3 do?", options=["Changes to (3,2)", "Error - tuples immutable", "Returns 3", "Nothing"], correct_index=1, topic="Data Structures", explanation="Tuples cannot be modified."),
    QuizQuestion(question="What does 'a' in {'a':1}.keys() return?", options=["True", "False", "1", "Error"], correct_index=0, topic="Data Structures", explanation="keys() returns a view; 'in' checks membership."),
    QuizQuestion(question="What does list(dict.fromkeys([1,2,1,3])) produce?", options=["[1,2,1,3]", "[1,2,3]", "Error", "[1,2,3] (order preserved in 3.7+)"], correct_index=3, topic="Data Structures", explanation="fromkeys deduplicates; keys preserve order."),
    QuizQuestion(question="What does [1,2,3][::-1] return?", options=["[3,2,1]", "[1,2,3]", "Error", "[1]"], correct_index=0, topic="Data Structures", explanation="[::-1] reverses the list."),
    QuizQuestion(question="What does {1,2}.add(1) do?", options=["Adds 1", "No change (1 already in set)", "Error", "Returns {1,2}"], correct_index=1, topic="Data Structures", explanation="add(1) when 1 exists: set unchanged."),
    QuizQuestion(question="What does {1,2}.discard(3) do?", options=["KeyError", "Returns None, no error", "Removes 3", "Error"], correct_index=1, topic="Data Structures", explanation="discard() removes if present; no error if missing."),
    QuizQuestion(question="What does {1,2}.remove(3) do?", options=["KeyError", "Returns None", "Removes 3", "No change"], correct_index=0, topic="Data Structures", explanation="remove() raises KeyError if element missing."),
    QuizQuestion(question="What does [1,2,3][1:2] return?", options=["[2]", "[1,2]", "[2,3]", "2"], correct_index=0, topic="Data Structures", explanation="Slice [1:2] returns elements at index 1 only."),
    QuizQuestion(question="What does [1,2,3][:2] return?", options=["[1,2]", "[1,2,3]", "[2,3]", "Error"], correct_index=0, topic="Data Structures", explanation="[:2] is from start to index 2 (exclusive)."),
    QuizQuestion(question="What does [1,2,3][1:] return?", options=["[2,3]", "[1,2]", "[1,2,3]", "Error"], correct_index=0, topic="Data Structures", explanation="[1:] is from index 1 to end."),
    QuizQuestion(question="What does d.update({'a':1}) do?", options=["Returns new dict", "Updates d in place", "Error", "Replaces d"], correct_index=1, topic="Data Structures", explanation="update() merges key-value pairs into d."),
    QuizQuestion(question="What does [x for x in [1,2,3] if x>1] produce?", options=["[2,3]", "[1,2,3]", "Error", "[1]"], correct_index=0, topic="Data Structures", explanation="List comprehension with condition."),
    QuizQuestion(question="What does {x: x**2 for x in range(3)} produce?", options=["{0:0,2:4}", "{0:0,1:1,2:4}", "Error", "[0,1,4]"], correct_index=1, topic="Data Structures", explanation="Dict comprehension: 0→0, 1→1, 2→4."),
    QuizQuestion(question="What does (x for x in range(3)) create?", options=["[0,1,2]", "Generator", "Tuple", "Error"], correct_index=1, topic="Data Structures", explanation="Parentheses with for create a generator."),
    QuizQuestion(question="What does [1,2,3] * 2 produce?", options=["[2,4,6]", "[1,2,3,1,2,3]", "Error", "[1,2,3]"], correct_index=1, topic="Data Structures", explanation="List * n repeats the list."),
    QuizQuestion(question="What does {1,2} ^ {2,3} return?", options=["{1,3}", "{2}", "Error", "{1,2,3}"], correct_index=0, topic="Data Structures", explanation="^ is symmetric difference (elements in one but not both)."),
    QuizQuestion(question="What does 'hello'.split('l') return?", options=["['he','o']", "['he','','o']", "['h','e','l','l','o']", "Error"], correct_index=1, topic="Data Structures", explanation="split('l') splits on 'l'; 'hel'→'he'+''+'o'."),
    QuizQuestion(question="What does [1,2,3].insert(0, 0) do?", options=["Prepends 0", "Inserts 0 at index 0", "Both", "Error"], correct_index=2, topic="Data Structures", explanation="insert(0, 0) puts 0 at the beginning."),
    QuizQuestion(question="What does d.setdefault('a', 1) do when 'a' missing?", options=["Returns 1", "Sets d['a']=1 and returns 1", "Error", "Returns None"], correct_index=1, topic="Data Structures", explanation="setdefault sets if missing, returns value."),
    QuizQuestion(question="What does [1,2,3].pop(1) return?", options=["1", "2", "3", "Error"], correct_index=1, topic="Data Structures", explanation="pop(1) removes and returns element at index 1."),
    QuizQuestion(question="What does [1,2,3].pop() return?", options=["1", "2", "3", "Error"], correct_index=2, topic="Data Structures", explanation="pop() removes and returns last element."),
    QuizQuestion(question="What does frozenset([1,2]) allow?", options=["add(3)", "Mutable operations", "Nothing - immutable", "discard(1)"], correct_index=2, topic="Data Structures", explanation="frozenset is immutable; no add/discard."),
    QuizQuestion(question="What does [1,2,3].sort() return?", options=["[1,2,3]", "None", "True", "Error"], correct_index=1, topic="Data Structures", explanation="sort() sorts in place; returns None."),
    QuizQuestion(question="What does dict(zip(['a','b'],[1,2])) produce?", options=["{'a':1,'b':2}", "Error", "[('a',1),('b',2)]", "{}"], correct_index=0, topic="Data Structures", explanation="zip pairs keys with values; dict() builds dict."),
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
    QuizQuestion(question="What does divmod(10, 3) return?", options=["(3, 1)", "(3.33, 0)", "Error", "3"], correct_index=0, topic="Build-In Funcions", explanation="divmod returns (quotient, remainder): (3, 1)."),
    QuizQuestion(question="What does pow(2, 3) return?", options=["6", "8", "9", "5"], correct_index=1, topic="Build-In Funcions", explanation="pow(2,3) = 2**3 = 8."),
    QuizQuestion(question="What does all([True, True, False]) return?", options=["True", "False", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="all() returns False if any element is falsy."),
    QuizQuestion(question="What does any([False, False, True]) return?", options=["True", "False", "Error", "1"], correct_index=0, topic="Build-In Funcions", explanation="any() returns True if any element is truthy."),
    QuizQuestion(question="What does bin(5) return?", options=["'101'", "'0b101'", "101", "5"], correct_index=1, topic="Build-In Funcions", explanation="bin() returns binary string with 0b prefix."),
    QuizQuestion(question="What does oct(8) return?", options=["'8'", "'0o10'", "10", "Error"], correct_index=1, topic="Build-In Funcions", explanation="oct() returns octal string with 0o prefix."),
    QuizQuestion(question="What does chr(65) return?", options=["65", "'A'", "'65'", "Error"], correct_index=1, topic="Build-In Funcions", explanation="chr() returns character for Unicode code point."),
    QuizQuestion(question="What does ord('A') return?", options=["'A'", "65", "1", "Error"], correct_index=1, topic="Build-In Funcions", explanation="ord() returns Unicode code point of character."),
    QuizQuestion(question="What does isinstance(3.5, (int, float)) return?", options=["True", "False", "float", "Error"], correct_index=0, topic="Build-In Funcions", explanation="Second arg can be tuple of types."),
    QuizQuestion(question="What does hasattr(obj, 'x') return?", options=["Value of obj.x", "True if obj has attribute x", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="hasattr checks if attribute exists."),
    QuizQuestion(question="What does sum([1,2,3], 10) return?", options=["16", "6", "Error", "15"], correct_index=0, topic="Build-In Funcions", explanation="sum(iterable, start) adds start: 10+1+2+3=16."),
    QuizQuestion(question="What does min([3,1,4], key=abs) return for [3,-1,4]?", options=["3", "-1", "4", "1"], correct_index=1, topic="Build-In Funcions", explanation="key=abs: min by abs value; -1 has abs 1."),
    QuizQuestion(question="What does sorted([3,1,2], key=lambda x: -x) return?", options=["[1,2,3]", "[3,2,1]", "Error", "[3,1,2]"], correct_index=1, topic="Build-In Funcions", explanation="key=lambda x:-x sorts by negative (descending)."),
    QuizQuestion(question="What does range(10)[::2] produce when converted to list?", options=["[0,2,4,6,8]", "[1,3,5,7,9]", "Error", "[0,1,2,3,4]"], correct_index=0, topic="Build-In Funcions", explanation="Slicing range with step 2."),
    QuizQuestion(question="What does ' '.join(['a','b','c']) return?", options=["'abc'", "'a b c'", "'a','b','c'", "Error"], correct_index=1, topic="Build-In Funcions", explanation="join uses separator between elements."),
    QuizQuestion(question="What does repr('hi') return?", options=["'hi'", "'\\'hi\\''", "hi", "Error"], correct_index=1, topic="Build-In Funcions", explanation="repr returns string representation (with quotes)."),
    QuizQuestion(question="What does eval('1+2') return?", options=["'1+2'", "3", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="eval evaluates the string as Python expression."),
    QuizQuestion(question="What does type(1)() return?", options=["1", "0", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="type(1) is int; int() returns 0."),
    QuizQuestion(question="What does slice(1,5,2) create?", options=["[1,3]", "slice object", "Error", "[1,5]"], correct_index=1, topic="Build-In Funcions", explanation="slice() creates a slice object for indexing."),
    QuizQuestion(question="What does iter([1,2,3]) return?", options=["[1,2,3]", "Iterator", "Error", "1"], correct_index=1, topic="Build-In Funcions", explanation="iter() creates an iterator from iterable."),
    QuizQuestion(question="What does next(iter([1,2,3])) return?", options=["[1,2,3]", "1", "Error", "0"], correct_index=1, topic="Build-In Funcions", explanation="next() gets the first element from iterator."),
    QuizQuestion(question="What does bool(1) return?", options=["1", "True", "False", "Error"], correct_index=1, topic="Build-In Funcions", explanation="bool(1) is True (non-zero is truthy)."),
    QuizQuestion(question="What does float('inf') return?", options=["Error", "Infinity (float)", "0", "None"], correct_index=1, topic="Build-In Funcions", explanation="float('inf') is positive infinity."),
    QuizQuestion(question="What does complex(1, 2) return?", options=["1+2j", "(1,2)", "Error", "3"], correct_index=0, topic="Build-In Funcions", explanation="complex(real, imag) creates complex number."),
    QuizQuestion(question="What does format(42, 'b') return?", options=["'42'", "'101010'", "Error", "42"], correct_index=1, topic="Build-In Funcions", explanation="'b' format specifier gives binary."),
    QuizQuestion(question="What does vars() return in a function?", options=["Global vars", "Local variables", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="vars() returns __dict__ of local scope."),
    QuizQuestion(question="What does dir() return?", options=["List of names in current scope", "Directory path", "Error", "None"], correct_index=0, topic="Build-In Funcions", explanation="dir() returns list of names in scope."),
    QuizQuestion(question="What does id(x) return?", options=["Type of x", "Unique identity (memory address)", "Value of x", "Error"], correct_index=1, topic="Build-In Funcions", explanation="id() returns unique integer identity."),
    QuizQuestion(question="What does hash('hello') return?", options=["'hello'", "Integer hash", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="hash() returns hash value (int)."),
    QuizQuestion(question="What does input() return?", options=["Nothing", "String from user", "Integer", "Error"], correct_index=1, topic="Build-In Funcions", explanation="input() reads and returns a string."),
    QuizQuestion(question="What does print(1, 2, sep='-') output?", options=["1 2", "1-2", "12", "Error"], correct_index=1, topic="Build-In Funcions", explanation="sep='-' puts '-' between arguments."),
    QuizQuestion(question="What does open('f.txt').read() return?", options=["File object", "File contents as string", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="read() returns file contents."),
    QuizQuestion(question="What does len(range(5)) return?", options=["5", "4", "Error", "0"], correct_index=0, topic="Build-In Funcions", explanation="len(range(5)) is 5."),
    QuizQuestion(question="What does all([]) return?", options=["False", "True", "Error", "None"], correct_index=1, topic="Build-In Funcions", explanation="all() of empty iterable is True."),
    QuizQuestion(question="What does any([]) return?", options=["False", "True", "Error", "None"], correct_index=0, topic="Build-In Funcions", explanation="any() of empty iterable is False."),
    QuizQuestion(question="What does round(2.5) return in Python 3?", options=["2", "3", "2.5", "2.0"], correct_index=0, topic="Build-In Funcions", explanation="Banker's rounding: 2.5 rounds to 2."),
    QuizQuestion(question="What does '{}'.format(42) return?", options=["'42'", "'{}'", "Error", "42"], correct_index=0, topic="Build-In Funcions", explanation="format() formats the value into the string."),
    QuizQuestion(question="What does bytes([65, 66]) return?", options=["'AB'", "b'AB'", "Error", "[65,66]"], correct_index=1, topic="Build-In Funcions", explanation="bytes() creates bytes from int sequence."),
    QuizQuestion(question="What does bytearray([1,2,3]) create?", options=["Mutable bytes", "Immutable bytes", "List", "Error"], correct_index=0, topic="Build-In Funcions", explanation="bytearray is mutable sequence of bytes."),
    QuizQuestion(question="What does memoryview(b'hi') return?", options=["'hi'", "Memory view object", "Error", "b'hi'"], correct_index=1, topic="Build-In Funcions", explanation="memoryview() creates memory view."),
    QuizQuestion(question="What does property() do?", options=["Creates a property descriptor", "Returns value", "Error", "Creates attribute"], correct_index=0, topic="Build-In Funcions", explanation="property() creates a property for classes."),
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
    QuizQuestion(question="What does __eq__ define?", options=["Equality comparison (==)", "Assignment", "Less than", "Greater than"], correct_index=0, topic="Classes", explanation="__eq__ is called for == comparison."),
    QuizQuestion(question="What does __lt__ define?", options=["Less than (<)", "Greater than", "Equal", "Length"], correct_index=0, topic="Classes", explanation="__lt__ is called for < comparison."),
    QuizQuestion(question="What does __add__ define?", options=["The + operator", "Assignment", "Append", "Import"], correct_index=0, topic="Classes", explanation="__add__ is called for obj + other."),
    QuizQuestion(question="What does __getitem__ allow?", options=["Indexing obj[i]", "Getting attribute", "Calling obj()", "Iteration only"], correct_index=0, topic="Classes", explanation="__getitem__ enables obj[key] syntax."),
    QuizQuestion(question="What does __iter__ return?", options=["The object itself", "An iterator", "A list", "Error"], correct_index=1, topic="Classes", explanation="__iter__ should return an iterator."),
    QuizQuestion(question="What does __next__ do?", options=["Returns next item", "Resets iterator", "Returns None", "Raises StopIteration when done"], correct_index=3, topic="Classes", explanation="__next__ raises StopIteration when exhausted."),
    QuizQuestion(question="What does __call__ allow?", options=["obj() to call the instance", "obj.attr", "obj[i]", "obj + x"], correct_index=0, topic="Classes", explanation="__call__ makes instances callable."),
    QuizQuestion(question="What does __del__ do?", options=["Deletes an attribute", "Called when object is garbage collected", "Deletes the class", "Nothing"], correct_index=1, topic="Classes", explanation="__del__ is the destructor."),
    QuizQuestion(question="What does __enter__ and __exit__ define?", options=["Context manager (with statement)", "Loop control", "Import", "Exception"], correct_index=0, topic="Classes", explanation="__enter__/__exit__ enable 'with' statement."),
    QuizQuestion(question="What does @property do?", options=["Makes a method callable as attribute", "Creates a class attribute", "Nothing", "Error"], correct_index=0, topic="Classes", explanation="property makes method accessible as obj.attr."),
    QuizQuestion(question="What does MRO mean?", options=["Method Resolution Order", "Multiple Return Option", "Module Reference Object", "Method Return Order"], correct_index=0, topic="Classes", explanation="MRO determines method lookup order in inheritance."),
    QuizQuestion(question="What does super() do in inheritance?", options=["Calls parent's method", "Creates superclass", "Raises error", "Returns self"], correct_index=0, topic="Classes", explanation="super() delegates to parent class."),
    QuizQuestion(question="What does issubclass(Child, Parent) return?", options=["True if Child inherits Parent", "The parent class", "Error", "False"], correct_index=0, topic="Classes", explanation="issubclass checks inheritance."),
    QuizQuestion(question="What does isinstance(obj, Class) check?", options=["If obj is instance of Class", "If obj is subclass", "If obj has attribute", "If obj equals Class"], correct_index=0, topic="Classes", explanation="isinstance checks if obj is instance."),
    QuizQuestion(question="What does __slots__ do?", options=["Limits attributes to save memory", "Creates slots", "Error", "Nothing"], correct_index=0, topic="Classes", explanation="__slots__ restricts instance attributes."),
    QuizQuestion(question="What does __dict__ contain?", options=["Instance attributes", "Class attributes", "Module attributes", "Nothing"], correct_index=0, topic="Classes", explanation="__dict__ holds instance attributes."),
    QuizQuestion(question="What does __bases__ contain?", options=["Parent classes", "Child classes", "Methods", "Attributes"], correct_index=0, topic="Classes", explanation="__bases__ is tuple of base classes."),
    QuizQuestion(question="What does __mro__ contain?", options=["Method resolution order", "Methods", "Attributes", "Error"], correct_index=0, topic="Classes", explanation="__mro__ is the method resolution order."),
    QuizQuestion(question="What does __new__ do?", options=["Creates the instance", "Initializes the instance", "Both", "Nothing"], correct_index=0, topic="Classes", explanation="__new__ creates; __init__ initializes."),
    QuizQuestion(question="What does __init__ receive?", options=["The new instance (self)", "The class", "Nothing", "Error"], correct_index=0, topic="Classes", explanation="__init__ receives self (the instance)."),
    QuizQuestion(question="What does __hash__ define?", options=["Hash for use in set/dict", "String representation", "Length", "Equality"], correct_index=0, topic="Classes", explanation="__hash__ enables use as dict key."),
    QuizQuestion(question="What does __bool__ define?", options=["Truth value for bool(obj)", "Boolean attribute", "Comparison", "Nothing"], correct_index=0, topic="Classes", explanation="__bool__ is called for bool(obj)."),
    QuizQuestion(question="What does __contains__ define?", options=["'in' operator", "'not in'", "Membership", "All of the above"], correct_index=3, topic="Classes", explanation="__contains__ enables 'in' operator."),
    QuizQuestion(question="What does __getattr__ do?", options=["Called when attribute not found", "Gets any attribute", "Raises error", "Returns None"], correct_index=0, topic="Classes", explanation="__getattr__ is fallback for missing attributes."),
    QuizQuestion(question="What does __setattr__ do?", options=["Called when setting attribute", "Sets attribute", "Both", "Nothing"], correct_index=2, topic="Classes", explanation="__setattr__ intercepts attribute assignment."),
    QuizQuestion(question="What does __delattr__ do?", options=["Called when deleting attribute", "Deletes attribute", "Both", "Nothing"], correct_index=2, topic="Classes", explanation="__delattr__ intercepts del obj.attr."),
    QuizQuestion(question="What does abstract method mean?", options=["Must be overridden in subclass", "Cannot be called", "Empty method", "Error"], correct_index=0, topic="Classes", explanation="Abstract method has no implementation."),
    QuizQuestion(question="What does ABC stand for?", options=["Abstract Base Class", "Abstract Basic Class", "Attribute Base Class", "Nothing"], correct_index=0, topic="Classes", explanation="ABC = Abstract Base Class."),
    QuizQuestion(question="What does @abstractmethod do?", options=["Marks method as abstract", "Creates abstract class", "Both", "Nothing"], correct_index=0, topic="Classes", explanation="@abstractmethod marks method to override."),
    QuizQuestion(question="What does __repr__ aim for?", options=["Unambiguous representation", "User-friendly", "Both", "Neither"], correct_index=0, topic="Classes", explanation="__repr__ should be unambiguous for debugging."),
    QuizQuestion(question="What does __str__ aim for?", options=["User-friendly", "Unambiguous", "Both", "Neither"], correct_index=0, topic="Classes", explanation="__str__ is for end users."),
    QuizQuestion(question="What does __format__ define?", options=["format(obj, spec)", "str(obj)", "repr(obj)", "print(obj)"], correct_index=0, topic="Classes", explanation="__format__ is for format() function."),
    QuizQuestion(question="What does __getitem__ allow for?", options=["obj[key]", "obj.attr", "obj()", "obj + x"], correct_index=0, topic="Classes", explanation="__getitem__ enables indexing."),
    QuizQuestion(question="What does __setitem__ do?", options=["obj[key] = value", "obj.attr = value", "obj() = value", "Nothing"], correct_index=0, topic="Classes", explanation="__setitem__ enables assignment to index."),
    QuizQuestion(question="What does __delitem__ do?", options=["del obj[key]", "del obj.attr", "delete obj", "Nothing"], correct_index=0, topic="Classes", explanation="__delitem__ enables del obj[key]."),
    QuizQuestion(question="What does __iter__ need for 'for x in obj'?", options=["__iter__ returning iterator", "__next__", "Both", "Neither"], correct_index=2, topic="Classes", explanation="__iter__ returns iterator with __next__."),
    QuizQuestion(question="What does __radd__ define?", options=["other + obj (reversed)", "obj + other", "Addition", "Nothing"], correct_index=0, topic="Classes", explanation="__radd__ is for reverse add when left doesn't support."),
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
    QuizQuestion(question="What does 'r+' mode allow?", options=["Read only", "Read and write", "Write only", "Append only"], correct_index=1, topic="Files", explanation="'r+' opens for both reading and writing."),
    QuizQuestion(question="What does 'w+' mode do?", options=["Read and write, truncates", "Write only", "Append and read", "Error"], correct_index=0, topic="Files", explanation="'w+' truncates and allows read/write."),
    QuizQuestion(question="What does 'a+' mode do?", options=["Append and read", "Read only", "Overwrite", "Error"], correct_index=0, topic="Files", explanation="'a+' appends and allows reading."),
    QuizQuestion(question="What does file.tell() return?", options=["File name", "Current position (bytes)", "File size", "Line number"], correct_index=1, topic="Files", explanation="tell() returns current byte position."),
    QuizQuestion(question="What does file.seek(0, 2) do?", options=["Go to start", "Go to end", "Go to byte 2", "Error"], correct_index=1, topic="Files", explanation="seek(0, 2) - 2 means end of file."),
    QuizQuestion(question="What does file.read(5) return?", options=["5 lines", "5 bytes/chars", "First 5 words", "Error"], correct_index=1, topic="Files", explanation="read(n) reads up to n characters/bytes."),
    QuizQuestion(question="What does file.writelines(['a','b']) do?", options=["Write 'a' and 'b' with newlines", "Write 'ab'", "Write each string (no newlines added)", "Error"], correct_index=2, topic="Files", explanation="writelines writes each string without adding newlines."),
    QuizQuestion(question="What does file.flush() do?", options=["Closes file", "Writes buffer to disk", "Clears file", "Error"], correct_index=1, topic="Files", explanation="flush() writes buffered data to disk."),
    QuizQuestion(question="What does file.closed return?", options=["True if closed", "The close method", "Error", "None"], correct_index=0, topic="Files", explanation="closed is True when file is closed."),
    QuizQuestion(question="What does 't' in 'rt' mean?", options=["Text mode (default)", "Temp file", "Truncate", "Nothing"], correct_index=0, topic="Files", explanation="'t' is text mode."),
    QuizQuestion(question="What does 'rb' open?", options=["Binary read", "Text read", "Binary write", "Error"], correct_index=0, topic="Files", explanation="'rb' = read binary."),
    QuizQuestion(question="What does 'wb' open?", options=["Binary write", "Text write", "Binary read", "Error"], correct_index=0, topic="Files", explanation="'wb' = write binary."),
    QuizQuestion(question="What does encoding='utf-8' do in open()?", options=["Sets file encoding", "Reads as UTF-8", "Both", "Nothing"], correct_index=2, topic="Files", explanation="encoding specifies encoding for text mode."),
    QuizQuestion(question="What does newline='' do in open()?", options=["Disables newline translation", "Sets line ending", "Both", "Error"], correct_index=2, topic="Files", explanation="newline='' for binary-like behavior with text."),
    QuizQuestion(question="What does file.__enter__() return?", options=["The file object", "None", "True", "Error"], correct_index=0, topic="Files", explanation="'with' returns the file from __enter__."),
    QuizQuestion(question="What does file.read(1) return at EOF?", options=["''", "None", "Error", "Last char"], correct_index=0, topic="Files", explanation="read() returns empty string at end of file."),
    QuizQuestion(question="What does file.readline() return at EOF?", options=["''", "None", "Error", "Last line"], correct_index=0, topic="Files", explanation="readline() returns '' at end."),
    QuizQuestion(question="What does open('x').close() do?", options=["Opens and closes", "Closes the file", "Both", "Error"], correct_index=2, topic="Files", explanation="Opens, then close() releases the resource."),
    QuizQuestion(question="What does 'x' mode do?", options=["Exclusive create - fails if exists", "Creates new", "Opens for write", "Error"], correct_index=0, topic="Files", explanation="'x' creates only if file doesn't exist."),
    QuizQuestion(question="What does file.tell() after read()?", options=["Position after last read", "0", "File size", "Error"], correct_index=0, topic="Files", explanation="tell() gives current position in file."),
    QuizQuestion(question="What does file.seek(0) do?", options=["Go to start", "Go to end", "Read 0 bytes", "Error"], correct_index=0, topic="Files", explanation="seek(0) moves to beginning."),
    QuizQuestion(question="What does 'a' mode do if file exists?", options=["Overwrites", "Appends to end", "Reads first", "Error"], correct_index=1, topic="Files", explanation="'a' appends; doesn't truncate."),
    QuizQuestion(question="What does 'w' mode do if file exists?", options=["Overwrites", "Appends", "Error", "Reads"], correct_index=0, topic="Files", explanation="'w' truncates (overwrites) existing file."),
    QuizQuestion(question="What does file.read() return for empty file?", options=["''", "None", "Error", "[]"], correct_index=0, topic="Files", explanation="read() of empty file returns ''."),
    QuizQuestion(question="What does 'r' mode do if file missing?", options=["Creates file", "FileNotFoundError", "Returns None", "Creates empty"], correct_index=1, topic="Files", explanation="'r' raises FileNotFoundError if missing."),
    QuizQuestion(question="What does 'w' mode do if file missing?", options=["FileNotFoundError", "Creates file", "Error", "Returns None"], correct_index=1, topic="Files", explanation="'w' creates the file if it doesn't exist."),
    QuizQuestion(question="What does file.readable() return?", options=["True if open for reading", "Content", "Error", "None"], correct_index=0, topic="Files", explanation="readable() checks if file supports read."),
    QuizQuestion(question="What does file.writable() return?", options=["True if open for writing", "Content", "Error", "None"], correct_index=0, topic="Files", explanation="writable() checks if file supports write."),
    QuizQuestion(question="What does file.isatty() return?", options=["True if terminal", "File type", "Error", "None"], correct_index=0, topic="Files", explanation="isatty() checks if file is a TTY."),
    QuizQuestion(question="What does file.fileno() return?", options=["File descriptor number", "File name", "File size", "Error"], correct_index=0, topic="Files", explanation="fileno() returns OS file descriptor."),
    QuizQuestion(question="What does file.truncate(size) do?", options=["Resizes file to size", "Deletes file", "Reads size bytes", "Error"], correct_index=0, topic="Files", explanation="truncate() resizes file."),
    QuizQuestion(question="What does file.read(-1) do?", options=["Reads all", "Reads nothing", "Error", "Reads last byte"], correct_index=0, topic="Files", explanation="Negative or omitted reads until EOF."),
    QuizQuestion(question="What does 'U' mode do?", options=["Universal newlines (deprecated)", "Unicode", "Update", "Error"], correct_index=0, topic="Files", explanation="'U' was for universal newlines."),
    QuizQuestion(question="What does file.__exit__ do?", options=["Closes file", "Handles exceptions", "Both", "Nothing"], correct_index=2, topic="Files", explanation="__exit__ closes and handles cleanup."),
    QuizQuestion(question="What does open('f', encoding=None) do for text?", options=["Uses default encoding", "Binary mode", "Error", "UTF-8"], correct_index=0, topic="Files", explanation="None uses default (usually UTF-8)."),
    QuizQuestion(question="What does file.readline(10) do?", options=["Reads up to 10 chars", "Reads 10 lines", "Error", "Reads 10 bytes"], correct_index=0, topic="Files", explanation="readline(n) reads up to n chars."),
    QuizQuestion(question="What does 'rt' mode mean?", options=["Read text", "Read and write", "Replace text", "Error"], correct_index=0, topic="Files", explanation="'rt' = read text (default)."),
    QuizQuestion(question="What does file.readline() return for 'a\\nb\\n'?", options=["'a\\n'", "'a'", "'a\\nb\\n'", "Error"], correct_index=0, topic="Files", explanation="readline() returns one line including newline."),
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
    QuizQuestion(question="What does Path.home() return?", options=["Current dir", "User home directory", "Temp dir", "Error"], correct_index=1, topic="loop through files", explanation="home() returns user's home directory."),
    QuizQuestion(question="What does Path.exists() return?", options=["True if path exists", "File contents", "Error", "None"], correct_index=0, topic="loop through files", explanation="exists() checks if path exists."),
    QuizQuestion(question="What does Path.is_dir() return?", options=["True if directory", "True if file", "Error", "Path"], correct_index=0, topic="loop through files", explanation="is_dir() checks if it's a directory."),
    QuizQuestion(question="What does Path.is_absolute() return?", options=["True if absolute path", "True if exists", "Error", "Path"], correct_index=0, topic="loop through files", explanation="is_absolute() checks if path is absolute."),
    QuizQuestion(question="What does Path.resolve() return?", options=["Absolute resolved path", "Relative path", "Error", "None"], correct_index=0, topic="loop through files", explanation="resolve() resolves to absolute path."),
    QuizQuestion(question="What does Path.stat() return?", options=["File stats (size, etc)", "File contents", "Error", "Path"], correct_index=0, topic="loop through files", explanation="stat() returns os.stat_result."),
    QuizQuestion(question="What does Path.read_text() return?", options=["File contents as string", "Bytes", "Error", "None"], correct_index=0, topic="loop through files", explanation="read_text() reads and decodes."),
    QuizQuestion(question="What does Path.write_text('x') do?", options=["Reads file", "Writes string to file", "Error", "Appends"], correct_index=1, topic="loop through files", explanation="write_text() writes string to file."),
    QuizQuestion(question="What does Path.read_bytes() return?", options=["String", "bytes", "Error", "None"], correct_index=1, topic="loop through files", explanation="read_bytes() returns raw bytes."),
    QuizQuestion(question="What does Path.rename(new) do?", options=["Copies to new", "Renames/moves to new", "Error", "Deletes"], correct_index=1, topic="loop through files", explanation="rename() renames or moves."),
    QuizQuestion(question="What does Path.rmdir() do?", options=["Removes file", "Removes empty directory", "Error", "Removes all"], correct_index=1, topic="loop through files", explanation="rmdir() removes empty directory."),
    QuizQuestion(question="What does Path.with_suffix('.txt') do?", options=["Changes extension", "Adds suffix", "Error", "Nothing"], correct_index=0, topic="loop through files", explanation="with_suffix() returns path with new extension."),
    QuizQuestion(question="What does Path.with_name('new') do?", options=["Renames to new", "Returns path with new name", "Error", "Copies"], correct_index=1, topic="loop through files", explanation="with_name() returns path with new filename."),
    QuizQuestion(question="What does Path.match('*.py') return?", options=["True if matches pattern", "List of matches", "Error", "Path"], correct_index=0, topic="loop through files", explanation="match() checks if path matches pattern."),
    QuizQuestion(question="What does Path.rglob('*.py') do?", options=["Glob in current dir only", "Recursive glob", "Error", "Returns nothing"], correct_index=1, topic="loop through files", explanation="rglob() is recursive glob."),
    QuizQuestion(question="What does os.path.join('a','b') return?", options=["'a/b' or 'a\\\\b'", "'ab'", "Error", "'a'"], correct_index=0, topic="loop through files", explanation="join() joins with OS separator."),
    QuizQuestion(question="What does os.path.abspath('x') return?", options=["Absolute path of x", "Relative path", "Error", "None"], correct_index=0, topic="loop through files", explanation="abspath() returns absolute path."),
    QuizQuestion(question="What does os.path.basename('/a/b/c') return?", options=["'c'", "'/a/b'", "'a/b/c'", "Error"], correct_index=0, topic="loop through files", explanation="basename() returns last component."),
    QuizQuestion(question="What does os.path.dirname('/a/b/c') return?", options=["'/a/b'", "'c'", "'/a/b/c'", "Error"], correct_index=0, topic="loop through files", explanation="dirname() returns directory part."),
    QuizQuestion(question="What does os.path.split('/a/b/c') return?", options=["('/a/b','c')", "['a','b','c']", "Error", "'/a/b/c'"], correct_index=0, topic="loop through files", explanation="split() returns (head, tail)."),
    QuizQuestion(question="What does os.path.splitext('f.txt') return?", options=["('f','.txt')", "('f.txt','')", "Error", "'f'"], correct_index=0, topic="loop through files", explanation="splitext() splits extension."),
    QuizQuestion(question="What does os.getcwd() return?", options=["Current working directory", "Home dir", "Error", "None"], correct_index=0, topic="loop through files", explanation="getcwd() returns current directory."),
    QuizQuestion(question="What does os.chdir(path) do?", options=["Changes current directory", "Creates dir", "Error", "Deletes dir"], correct_index=0, topic="loop through files", explanation="chdir() changes working directory."),
    QuizQuestion(question="What does os.makedirs('a/b/c') do?", options=["Creates a only", "Creates a/b/c (all levels)", "Error", "Creates c only"], correct_index=1, topic="loop through files", explanation="makedirs() creates all intermediate dirs."),
    QuizQuestion(question="What does os.remove(path) do?", options=["Removes file", "Removes directory", "Error", "Renames"], correct_index=0, topic="loop through files", explanation="remove() deletes a file."),
    QuizQuestion(question="What does os.rename(src, dst) do?", options=["Copies", "Renames/moves", "Error", "Deletes"], correct_index=1, topic="loop through files", explanation="rename() renames or moves."),
    QuizQuestion(question="What does shutil.copy(src, dst) do?", options=["Copies file", "Moves file", "Error", "Deletes"], correct_index=0, topic="loop through files", explanation="shutil.copy copies a file."),
    QuizQuestion(question="What does shutil.copytree(src, dst) do?", options=["Copies directory tree", "Moves tree", "Error", "Deletes tree"], correct_index=0, topic="loop through files", explanation="copytree() recursively copies directory."),
    QuizQuestion(question="What does shutil.move(src, dst) do?", options=["Copies", "Moves (rename)", "Error", "Deletes"], correct_index=1, topic="loop through files", explanation="move() moves or renames."),
    QuizQuestion(question="What does shutil.rmtree(path) do?", options=["Removes directory tree", "Removes file", "Error", "Copies tree"], correct_index=0, topic="loop through files", explanation="rmtree() recursively deletes directory."),
    QuizQuestion(question="What does Path.touch() do?", options=["Creates empty file", "Opens file", "Error", "Deletes file"], correct_index=0, topic="loop through files", explanation="touch() creates empty file if not exists."),
    QuizQuestion(question="What does Path.samefile(other) return?", options=["True if same file", "True if same name", "Error", "Path"], correct_index=0, topic="loop through files", explanation="samefile() checks if paths point to same file."),
    QuizQuestion(question="What does Path.absolute() return?", options=["Absolute path", "Relative path", "Error", "None"], correct_index=0, topic="loop through files", explanation="absolute() returns absolute path."),
    QuizQuestion(question="What does Path.expanduser() do?", options=["Expands ~ to home", "Expands variables", "Error", "Nothing"], correct_index=0, topic="loop through files", explanation="expanduser() expands ~ to home dir."),
    QuizQuestion(question="What does Path.open() return?", options=["File object", "Path", "Error", "None"], correct_index=0, topic="loop through files", explanation="open() returns file object like open()."),
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
    QuizQuestion(question="What does plt.plot([1,2],[3,4]) create?", options=["Line from (1,3) to (2,4)", "Two lines", "Scatter", "Error"], correct_index=0, topic="Matplotlib 1", explanation="plot(x, y) creates line connecting points."),
    QuizQuestion(question="What does plt.scatter([1,2],[3,4]) create?", options=["Line plot", "Scatter plot", "Bar chart", "Error"], correct_index=1, topic="Matplotlib 1", explanation="scatter() creates scatter plot."),
    QuizQuestion(question="What does plt.bar([1,2],[3,4]) create?", options=["Line plot", "Bar chart", "Scatter", "Error"], correct_index=1, topic="Matplotlib 1", explanation="bar(x, height) creates bar chart."),
    QuizQuestion(question="What does plt.pie([1,2,3]) create?", options=["Line plot", "Pie chart", "Bar chart", "Error"], correct_index=1, topic="Matplotlib 1", explanation="pie() creates pie chart."),
    QuizQuestion(question="What does plt.fill_between(x, y1, y2) do?", options=["Fills area between curves", "Draws two lines", "Error", "Creates bar"], correct_index=0, topic="Matplotlib 1", explanation="fill_between fills area between y1 and y2."),
    QuizQuestion(question="What does plt.step(x, y) create?", options=["Step plot", "Line plot", "Bar chart", "Error"], correct_index=0, topic="Matplotlib 1", explanation="step() creates step plot."),
    QuizQuestion(question="What does plt.semilogy(x, y) do?", options=["Log y-axis", "Log x-axis", "Log both", "Linear"], correct_index=0, topic="Matplotlib 1", explanation="semilogy() uses log scale for y."),
    QuizQuestion(question="What does plt.loglog(x, y) do?", options=["Log both axes", "Log x only", "Log y only", "Linear"], correct_index=0, topic="Matplotlib 1", explanation="loglog() uses log scale for both."),
    QuizQuestion(question="What does plt.axhline(y=0) do?", options=["Horizontal line at y=0", "Vertical line", "Title", "Error"], correct_index=0, topic="Matplotlib 1", explanation="axhline() draws horizontal line."),
    QuizQuestion(question="What does plt.axvline(x=0) do?", options=["Vertical line at x=0", "Horizontal line", "Title", "Error"], correct_index=0, topic="Matplotlib 1", explanation="axvline() draws vertical line."),
    QuizQuestion(question="What does plt.axvspan(xmin, xmax) do?", options=["Vertical shaded region", "Horizontal span", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="axvspan() shades vertical region."),
    QuizQuestion(question="What does plt.twinx() create?", options=["Second y-axis on right", "Second x-axis", "Copy of plot", "Error"], correct_index=0, topic="Matplotlib 1", explanation="twinx() creates shared x, new y axis."),
    QuizQuestion(question="What does plt.tick_params() do?", options=["Configures tick appearance", "Sets ticks", "Removes ticks", "Error"], correct_index=0, topic="Matplotlib 1", explanation="tick_params() customizes ticks."),
    QuizQuestion(question="What does plt.xticks([1,2,3]) do?", options=["Sets x tick positions", "Sets y ticks", "Error", "Sets labels"], correct_index=0, topic="Matplotlib 1", explanation="xticks() sets tick positions."),
    QuizQuestion(question="What does plt.xticks([1,2], ['a','b']) do?", options=["Sets positions and labels", "Sets positions only", "Error", "Sets labels only"], correct_index=0, topic="Matplotlib 1", explanation="xticks(positions, labels) sets both."),
    QuizQuestion(question="What does plt.autoscale() do?", options=["Auto-adjust axis limits", "Scales figure", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="autoscale() adjusts limits to data."),
    QuizQuestion(question="What does plt.gca() return?", options=["Current axes", "Current figure", "Error", "None"], correct_index=0, topic="Matplotlib 1", explanation="gca() = get current axes."),
    QuizQuestion(question="What does plt.gcf() return?", options=["Current figure", "Current axes", "Error", "None"], correct_index=0, topic="Matplotlib 1", explanation="gcf() = get current figure."),
    QuizQuestion(question="What does plt.subplot(2,2,1) mean?", options=["2x2 grid, select 1st", "2 rows, 2 cols", "Error", "2 figures"], correct_index=0, topic="Matplotlib 1", explanation="subplot(rows, cols, index)."),
    QuizQuestion(question="What does plt.cla() do?", options=["Clears current axes", "Clears figure", "Closes", "Error"], correct_index=0, topic="Matplotlib 1", explanation="cla() clears current axes."),
    QuizQuestion(question="What does plt.rcParams do?", options=["Global style settings", "Current plot", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="rcParams holds default settings."),
    QuizQuestion(question="What does plt.style.use('ggplot') do?", options=["Uses ggplot style", "Creates ggplot", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="style.use() sets style."),
    QuizQuestion(question="What does plt.plot(..., linestyle='--') do?", options=["Dashed line", "Solid line", "Dotted", "Error"], correct_index=0, topic="Matplotlib 1", explanation="linestyle='--' gives dashed line."),
    QuizQuestion(question="What does plt.plot(..., linewidth=2) do?", options=["Thicker line", "Two lines", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="linewidth sets line thickness."),
    QuizQuestion(question="What does plt.plot(..., marker='o') do?", options=["Adds circle markers", "Adds line", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="marker='o' adds circle markers."),
    QuizQuestion(question="What does plt.plot(..., alpha=0.5) do?", options=["50% transparency", "Sets color", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="alpha sets transparency 0-1."),
    QuizQuestion(question="What does plt.fill(x, y) do?", options=["Fills under curve", "Draws line", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="fill() fills polygon under curve."),
    QuizQuestion(question="What does plt.errorbar(x, y, yerr=e) do?", options=["Adds error bars", "Adds line", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="errorbar() adds error bars."),
    QuizQuestion(question="What does plt.stem(x, y) create?", options=["Stem plot", "Line plot", "Bar chart", "Error"], correct_index=0, topic="Matplotlib 1", explanation="stem() creates stem plot."),
    QuizQuestion(question="What does plt.boxplot(data) create?", options=["Box plot", "Line plot", "Bar chart", "Error"], correct_index=0, topic="Matplotlib 1", explanation="boxplot() creates box-and-whisker."),
    QuizQuestion(question="What does plt.violinplot(data) create?", options=["Violin plot", "Line plot", "Error", "Bar chart"], correct_index=0, topic="Matplotlib 1", explanation="violinplot() creates violin plot."),
    QuizQuestion(question="What does plt.imshow(arr) do?", options=["Displays image/array", "Creates bar", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="imshow() displays 2D array as image."),
    QuizQuestion(question="What does plt.pcolormesh(X, Y, Z) do?", options=["Pseudocolor plot", "Line plot", "Error", "Scatter"], correct_index=0, topic="Matplotlib 1", explanation="pcolormesh() creates pseudocolor plot."),
    QuizQuestion(question="What does plt.contour(X, Y, Z) create?", options=["Contour lines", "Surface", "Error", "Scatter"], correct_index=0, topic="Matplotlib 1", explanation="contour() creates contour plot."),
    QuizQuestion(question="What does plt.contourf(X, Y, Z) create?", options=["Filled contours", "Line contours", "Error", "Surface"], correct_index=0, topic="Matplotlib 1", explanation="contourf() creates filled contours."),
    QuizQuestion(question="What does plt.plot(..., color='red') do?", options=["Sets line color", "Sets fill", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="color= sets the line color."),
    QuizQuestion(question="What does plt.plot(..., label='A') do?", options=["Adds label for legend", "Sets title", "Error", "Nothing"], correct_index=0, topic="Matplotlib 1", explanation="label= adds entry for legend."),
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
    QuizQuestion(question="What does fig, axes = plt.subplots(2, 2) give?", options=["2x2 array of axes", "One axes", "Error", "4 figures"], correct_index=0, topic="Matplotlib 2", explanation="Returns (fig, axes_array)."),
    QuizQuestion(question="What does axes.flatten() do?", options=["Flattens 2D axes to 1D", "Flattens figure", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="flatten() gives 1D array of axes."),
    QuizQuestion(question="What does ax.set_title('x') do?", options=["Sets subplot title", "Sets figure title", "Error", "Sets axis label"], correct_index=0, topic="Matplotlib 2", explanation="set_title() sets axes title."),
    QuizQuestion(question="What does ax.set_xlabel('x') do?", options=["Sets x-axis label", "Sets title", "Error", "Sets y label"], correct_index=0, topic="Matplotlib 2", explanation="set_xlabel() sets x-axis label."),
    QuizQuestion(question="What does ax.set_yscale('log') do?", options=["Log scale for y", "Log scale for x", "Error", "Linear"], correct_index=0, topic="Matplotlib 2", explanation="set_yscale() sets y-axis scale."),
    QuizQuestion(question="What does ax.invert_xaxis() do?", options=["Reverses x-axis", "Reverses y-axis", "Error", "Inverts colors"], correct_index=0, topic="Matplotlib 2", explanation="invert_xaxis() reverses x direction."),
    QuizQuestion(question="What does ax.set_xlim(0, 10) do?", options=["Sets x limits", "Sets y limits", "Error", "Sets title"], correct_index=0, topic="Matplotlib 2", explanation="set_xlim() sets x-axis range."),
    QuizQuestion(question="What does ax.set_ylim(0, 10) do?", options=["Sets y limits", "Sets x limits", "Error", "Sets title"], correct_index=0, topic="Matplotlib 2", explanation="set_ylim() sets y-axis range."),
    QuizQuestion(question="What does ax.legend() do?", options=["Adds legend", "Adds title", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="legend() displays legend."),
    QuizQuestion(question="What does ax.grid(True) do?", options=["Adds grid lines", "Creates grid of subplots", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="grid(True) shows grid."),
    QuizQuestion(question="What does ax.annotate(...) do?", options=["Adds annotation", "Adds title", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="annotate() adds text with optional arrow."),
    QuizQuestion(question="What does ax.text(x, y, s) do?", options=["Adds text at (x,y)", "Adds title", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="text() places text at coordinates."),
    QuizQuestion(question="What does fig.add_axes([0.1,0.1,0.8,0.8]) do?", options=["Adds axes at position", "Adds subplot", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="add_axes() adds axes with [left,bottom,w,h]."),
    QuizQuestion(question="What does ax.twinx() create?", options=["Second y-axis", "Second x-axis", "Error", "Copy"], correct_index=0, topic="Matplotlib 2", explanation="twinx() creates shared x, new y."),
    QuizQuestion(question="What does ax.twiny() create?", options=["Second x-axis", "Second y-axis", "Error", "Copy"], correct_index=0, topic="Matplotlib 2", explanation="twiny() creates shared y, new x."),
    QuizQuestion(question="What does ax.set_facecolor('white') do?", options=["Sets axes background", "Sets figure background", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_facecolor() sets axes background."),
    QuizQuestion(question="What does ax.spines['top'].set_visible(False) do?", options=["Hides top spine", "Hides all", "Error", "Shows top"], correct_index=0, topic="Matplotlib 2", explanation="Hides the top axis line."),
    QuizQuestion(question="What does ax.set_aspect('equal') do?", options=["Equal aspect ratio", "Sets size", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_aspect() sets aspect ratio."),
    QuizQuestion(question="What does fig.savefig('out.png', dpi=150) do?", options=["Saves with 150 DPI", "Saves at 150px", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="dpi= sets resolution."),
    QuizQuestion(question="What does fig.set_size_inches(10, 5) do?", options=["Sets figure size", "Sets axes size", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_size_inches() sets figure dimensions."),
    QuizQuestion(question="What does ax.set_xticks([1,2,3]) do?", options=["Sets tick positions", "Sets labels", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_xticks() sets x tick positions."),
    QuizQuestion(question="What does ax.set_xticklabels(['a','b','c']) do?", options=["Sets tick labels", "Sets positions", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_xticklabels() sets label text."),
    QuizQuestion(question="What does ax.tick_params(axis='x', rotation=45) do?", options=["Rotates x labels 45°", "Rotates y labels", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="tick_params() customizes ticks."),
    QuizQuestion(question="What does ax.get_xlim() return?", options=["(left, right) tuple", "List", "Error", "None"], correct_index=0, topic="Matplotlib 2", explanation="get_xlim() returns current x limits."),
    QuizQuestion(question="What does ax.get_ylim() return?", options=["(bottom, top) tuple", "List", "Error", "None"], correct_index=0, topic="Matplotlib 2", explanation="get_ylim() returns current y limits."),
    QuizQuestion(question="What does ax.clear() do?", options=["Clears axes", "Clears figure", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="clear() removes all from axes."),
    QuizQuestion(question="What does ax.plot() add to?", options=["That axes", "New figure", "Error", "All axes"], correct_index=0, topic="Matplotlib 2", explanation="ax.plot() adds to that axes."),
    QuizQuestion(question="What does fig.axes return?", options=["List of axes", "Current axes", "Error", "None"], correct_index=0, topic="Matplotlib 2", explanation="fig.axes is list of axes in figure."),
    QuizQuestion(question="What does plt.subplot(2,1,1) then plt.subplot(2,1,2) do?", options=["Creates 2 stacked subplots", "Creates 2 side by side", "Error", "One subplot"], correct_index=0, topic="Matplotlib 2", explanation="2,1 = 2 rows 1 col; stacked."),
    QuizQuestion(question="What does ax.secondary_xaxis() create?", options=["Second x-axis", "Second y-axis", "Error", "Copy"], correct_index=0, topic="Matplotlib 2", explanation="secondary_xaxis() adds second x-axis."),
    QuizQuestion(question="What does fig.canvas.draw() do?", options=["Redraws figure", "Saves figure", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="draw() forces redraw."),
    QuizQuestion(question="What does plt.pause(0.1) do?", options=["Pauses for 0.1 sec", "Updates display", "Both", "Error"], correct_index=2, topic="Matplotlib 2", explanation="pause() updates display and waits."),
    QuizQuestion(question="What does ax.set_zorder(10) do?", options=["Sets drawing order", "Sets z-axis", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_zorder() controls layering."),
    QuizQuestion(question="What does ax.set_position() do?", options=["Sets axes position", "Sets figure position", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_position() sets axes bounds."),
    QuizQuestion(question="What does fig.subplots_adjust() do?", options=["Adjusts subplot spacing", "Adds subplots", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="subplots_adjust() changes spacing."),
    QuizQuestion(question="What does ax.set_anchor() do?", options=["Sets axes anchor", "Sets position", "Error", "Nothing"], correct_index=0, topic="Matplotlib 2", explanation="set_anchor() sets anchor point."),
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
    QuizQuestion(question="What does fontsize=14 do in annotate?", options=["Sets text size", "Sets arrow size", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="fontsize= sets text size."),
    QuizQuestion(question="What does color='red' do in text?", options=["Sets text color", "Sets background", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="color= sets text color."),
    QuizQuestion(question="What does arrowprops=dict(arrowstyle='->') do?", options=["Sets arrow style", "Removes arrow", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="arrowprops configures the arrow."),
    QuizQuestion(question="What does bbox=dict(facecolor='yellow') do?", options=["Yellow background box", "Yellow text", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="bbox adds background box."),
    QuizQuestion(question="What does fontfamily='monospace' do?", options=["Uses monospace font", "Sets font", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="fontfamily= sets font family."),
    QuizQuestion(question="What does fontstyle='italic' do?", options=["Italic text", "Bold text", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="fontstyle= sets italic."),
    QuizQuestion(question="What does verticalalignment='top' do?", options=["Aligns text to top", "Aligns to bottom", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="verticalalignment sets vertical alignment."),
    QuizQuestion(question="What does horizontalalignment='center' do?", options=["Centers text horizontally", "Centers vertically", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="horizontalalignment sets horizontal alignment."),
    QuizQuestion(question="What does rotation=45 do in text?", options=["Rotates text 45°", "Rotates axes", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="rotation= rotates text."),
    QuizQuestion(question="What does xycoords='axes fraction' mean?", options=["xy in 0-1 of axes", "xy in data coords", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="axes fraction uses 0-1 relative to axes."),
    QuizQuestion(question="What does textcoords='offset points' mean?", options=["Offset from xy in points", "Data coords", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="offset points for text position."),
    QuizQuestion(question="What does connectionstyle='arc3' do?", options=["Curved arrow", "Straight arrow", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="connectionstyle sets arrow path."),
    QuizQuestion(question="What does shrinkA=10 do in arrowprops?", options=["Shrinks arrow at start", "Shrinks at end", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="shrinkA shortens arrow at start."),
    QuizQuestion(question="What does multialignment='center' do?", options=["Centers multiline text", "Centers single line", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="multialignment for multiline."),
    QuizQuestion(question="What does wrap=True do in text?", options=["Wraps long text", "Wraps figure", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="wrap= wraps text to fit."),
    QuizQuestion(question="What does clip_on=True do?", options=["Clips text to axes", "Shows outside", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="clip_on clips to axes bounds."),
    QuizQuestion(question="What does zorder=10 do?", options=["Draws on top", "Draws below", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="zorder controls layering."),
    QuizQuestion(question="What does ax.annotate(...) add?", options=["Text with optional arrow", "Arrow only", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="annotate adds text with optional arrow."),
    QuizQuestion(question="What does plt.figtext(0.5, 0.5, 'x') do?", options=["Adds text to figure", "Adds to axes", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="figtext adds text in figure coords."),
    QuizQuestion(question="What does 'axes fraction' mean?", options=["0-1 relative to axes", "Data coords", "Error", "Pixels"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="0,0=bottom-left, 1,1=top-right."),
    QuizQuestion(question="What does 'figure fraction' mean?", options=["0-1 relative to figure", "Axes coords", "Error", "Pixels"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="0-1 relative to figure."),
    QuizQuestion(question="What does 'data' mean for coords?", options=["Data coordinates", "Figure coords", "Error", "Pixels"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="data = plot data coordinates."),
    QuizQuestion(question="What does 'offset points' mean?", options=["Offset in points from xy", "Pixels", "Error", "Data"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="Offset in typographic points."),
    QuizQuestion(question="What does arrowstyle='fancy' do?", options=["Fancy arrow", "Simple arrow", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="arrowstyle sets arrow appearance."),
    QuizQuestion(question="What does bbox=dict(alpha=0.5) do?", options=["50% transparent box", "Solid box", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="alpha sets box transparency."),
    QuizQuestion(question="What does 'upper' in va='upper' mean?", options=["Align to top", "Align to bottom", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="va='upper' aligns to top."),
    QuizQuestion(question="What does 'right' in ha='right' mean?", options=["Align to right", "Align to left", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="ha='right' aligns to right."),
    QuizQuestion(question="What does fontvariant='small-caps' do?", options=["Small caps text", "Small font", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="fontvariant sets small caps."),
    QuizQuestion(question="What does usetex=True do?", options=["Use LaTeX rendering", "Use plain text", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="usetex uses LaTeX for math."),
    QuizQuestion(question="What does math_text='math' do?", options=["Uses mathtext", "Uses LaTeX", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="math_text for math rendering."),
    QuizQuestion(question="What does 'lower' in va='lower' mean?", options=["Align to bottom", "Align to top", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="va='lower' aligns to bottom."),
    QuizQuestion(question="What does 'left' in ha='left' mean?", options=["Align to left", "Align to right", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="ha='left' aligns to left."),
    QuizQuestion(question="What does 'center' in va='center' mean?", options=["Vertical center", "Horizontal center", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="va='center' vertically centers."),
    QuizQuestion(question="What does 'baseline' in va='baseline' mean?", options=["Align to baseline", "Align to top", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="va='baseline' aligns to text baseline."),
    QuizQuestion(question="What does picker=True do?", options=["Makes text pickable", "Picks color", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="picker enables mouse events."),
    QuizQuestion(question="What does in_layout=True do?", options=["Include in layout", "Exclude from layout", "Error", "Nothing"], correct_index=0, topic="Matplotlib Exercise - plt.text", explanation="in_layout affects tight_layout."),
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
    QuizQuestion(question="What does df.plot(kind='kde') create?", options=["Kernel density plot", "Bar chart", "Line plot", "Error"], correct_index=0, topic="Pandas & Matplotlib", explanation="kind='kde' creates kernel density estimate."),
    QuizQuestion(question="What does df.plot(kind='area') create?", options=["Area chart", "Bar chart", "Line plot", "Error"], correct_index=0, topic="Pandas & Matplotlib", explanation="kind='area' creates area chart."),
    QuizQuestion(question="What does df.plot(kind='line') create?", options=["Line plot", "Bar chart", "Scatter", "Error"], correct_index=0, topic="Pandas & Matplotlib", explanation="kind='line' creates line plot."),
    QuizQuestion(question="What does df.plot(kind='barh') create?", options=["Horizontal bar chart", "Vertical bar chart", "Bar chart", "Error"], correct_index=0, topic="Pandas & Matplotlib", explanation="kind='barh' creates horizontal bars."),
    QuizQuestion(question="What does df.plot(kind='density') create?", options=["Density plot", "Bar chart", "Error", "Scatter"], correct_index=0, topic="Pandas & Matplotlib", explanation="kind='density' is alias for kde."),
    QuizQuestion(question="What does df.plot(kind='scatter', x='a', y='b') need?", options=["x and y columns", "Nothing", "Error", "kind only"], correct_index=0, topic="Pandas & Matplotlib", explanation="Scatter requires x= and y= to specify columns."),
    QuizQuestion(question="What does df.plot(kind='pie') use?", options=["Index as labels", "First column", "Error", "All columns"], correct_index=0, topic="Pandas & Matplotlib", explanation="Pie uses index for labels by default."),
    QuizQuestion(question="What does df.plot(kind='bar', stacked=True) do?", options=["Stacks bars", "Side by side", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="stacked=True stacks bars vertically."),
    QuizQuestion(question="What does df.plot(kind='bar', subplots=True) do?", options=["One subplot per column", "One plot", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="subplots=True creates one subplot per column."),
    QuizQuestion(question="What does df.plot(kind='line', use_index=True) do?", options=["Uses index as x-axis", "Uses first column", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="use_index=True uses index for x."),
    QuizQuestion(question="What does df.plot(kind='bar', rot=45) do?", options=["Rotates x labels 45°", "Rotates bars", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="rot= rotates tick labels."),
    QuizQuestion(question="What does df.plot(kind='line', style='--') do?", options=["Dashed line", "Solid line", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="style= sets line style."),
    QuizQuestion(question="What does df.plot(kind='line', color='red') do?", options=["Red line", "Red bar", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="color= sets line color."),
    QuizQuestion(question="What does df.plot(kind='bar', width=0.8) do?", options=["Sets bar width", "Sets figure width", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="width= sets bar width."),
    QuizQuestion(question="What does df.plot(kind='line', marker='o') do?", options=["Adds circle markers", "Adds line", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="marker= adds markers."),
    QuizQuestion(question="What does df.plot(kind='line', title='My Plot') do?", options=["Sets title", "Sets x label", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="title= sets plot title."),
    QuizQuestion(question="What does df.plot(kind='bar', figsize=(10,5)) do?", options=["Sets figure size", "Sets bar size", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="figsize= sets figure dimensions."),
    QuizQuestion(question="What does df.plot(kind='line', grid=True) do?", options=["Adds grid", "Creates grid", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="grid=True adds grid lines."),
    QuizQuestion(question="What does df.plot(kind='bar', alpha=0.7) do?", options=["70% transparency", "Solid bars", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="alpha= sets transparency."),
    QuizQuestion(question="What does df.plot(kind='line', logy=True) do?", options=["Log y-axis", "Log x-axis", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="logy=True uses log scale for y."),
    QuizQuestion(question="What does df.plot(kind='line', logx=True) do?", options=["Log x-axis", "Log y-axis", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="logx=True uses log scale for x."),
    QuizQuestion(question="What does df.plot(kind='bar', align='edge') do?", options=["Aligns bars to edge", "Centers bars", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="align= sets bar alignment."),
    QuizQuestion(question="What does df.plot(kind='line', secondary_y='col') do?", options=["Plots col on second y-axis", "Plots twice", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="secondary_y= uses second y-axis."),
    QuizQuestion(question="What does df.plot(kind='bar', table=True) do?", options=["Adds table below", "Creates table", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="table=True adds data table."),
    QuizQuestion(question="What does df.plot(kind='line', xlim=(0,10)) do?", options=["Sets x limits", "Sets y limits", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="xlim= sets x-axis range."),
    QuizQuestion(question="What does df.plot(kind='line', ylim=(0,10)) do?", options=["Sets y limits", "Sets x limits", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="ylim= sets y-axis range."),
    QuizQuestion(question="What does df.plot(kind='bar', colormap='viridis') do?", options=["Uses viridis colormap", "Sets color", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="colormap= sets color scheme."),
    QuizQuestion(question="What does df.plot(kind='line', sharex=True) do?", options=["Shares x-axis", "Shares y-axis", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="sharex= shares x-axis."),
    QuizQuestion(question="What does df.plot(kind='line', sharey=True) do?", options=["Shares y-axis", "Shares x-axis", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="sharey= shares y-axis."),
    QuizQuestion(question="What does df.plot(kind='bar', layout=(2,2)) do?", options=["2x2 subplot layout", "Figure layout", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="layout= sets subplot grid."),
    QuizQuestion(question="What does df.plot(kind='line', fontsize=12) do?", options=["Sets font size", "Sets figure size", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="fontsize= sets text size."),
    QuizQuestion(question="What does df.plot(kind='bar', xticks=range(5)) do?", options=["Sets x tick positions", "Sets y ticks", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="xticks= sets tick positions."),
    QuizQuestion(question="What does df.plot(kind='line', yticks=range(5)) do?", options=["Sets y tick positions", "Sets x ticks", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="yticks= sets tick positions."),
    QuizQuestion(question="What does df.plot(kind='bar', stacked=True, bottom=df2) do?", options=["Uses df2 as bottom", "Adds df2", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="bottom= sets bottom of stacked bars."),
    QuizQuestion(question="What does df.plot(kind='line', drawstyle='steps') do?", options=["Step plot", "Line plot", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="drawstyle='steps' creates step plot."),
    QuizQuestion(question="What does df.plot(kind='bar', edgecolor='black') do?", options=["Black bar edges", "Black background", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="edgecolor= sets bar edge color."),
    QuizQuestion(question="What does df.plot(kind='line', linestyle='--') do?", options=["Dashed line", "Solid line", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="linestyle= sets line style."),
    QuizQuestion(question="What does df.plot(kind='line', linewidth=2) do?", options=["Thicker line", "Two lines", "Error", "Nothing"], correct_index=0, topic="Pandas & Matplotlib", explanation="linewidth= sets line thickness."),
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
    QuizQuestion(question="What does df.groupby('col').max() return?", options=["Max per group", "Single max", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="max() returns max per group per column."),
    QuizQuestion(question="What does df.groupby('col').min() return?", options=["Min per group", "Single min", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="min() returns min per group."),
    QuizQuestion(question="What does df.groupby('col').first() return?", options=["First row per group", "First group", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="first() returns first row of each group."),
    QuizQuestion(question="What does df.groupby('col').last() return?", options=["Last row per group", "Last group", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="last() returns last row of each group."),
    QuizQuestion(question="What does df.groupby('col').nth(0) return?", options=["First row per group", "Row 0", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="nth(n) returns nth row per group."),
    QuizQuestion(question="What does df.groupby('col').nunique() return?", options=["Count of unique per group", "Unique values", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="nunique() counts unique values per group."),
    QuizQuestion(question="What does df.groupby('col').describe() return?", options=["Stats per group", "Single stats", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="describe() gives stats per group."),
    QuizQuestion(question="What does df.groupby('col').apply(func) do?", options=["Applies func to each group", "Applies to whole df", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="apply() runs func on each group."),
    QuizQuestion(question="What does df.groupby('col').transform(func) do?", options=["Transforms each group, same shape", "Transforms whole df", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="transform() returns same shape as input."),
    QuizQuestion(question="What does df.groupby('col').filter(func) do?", options=["Keeps groups where func True", "Filters rows", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="filter() keeps groups where func returns True."),
    QuizQuestion(question="What does df.groupby('col').head(2) return?", options=["First 2 rows per group", "First 2 groups", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="head(n) returns first n rows per group."),
    QuizQuestion(question="What does df.groupby('col').tail(2) return?", options=["Last 2 rows per group", "Last 2 groups", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="tail(n) returns last n rows per group."),
    QuizQuestion(question="What does df.groupby('col').get_group('x') return?", options=["Rows where col=='x'", "Group x", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="get_group() returns one group."),
    QuizQuestion(question="What does df.groupby('col').groups return?", options=["Dict of group name -> indices", "List of groups", "Error", "DataFrame"], correct_index=0, topic="Pandas 2", explanation="groups is dict mapping name to indices."),
    QuizQuestion(question="What does df.groupby('col').ngroups return?", options=["Number of groups", "Group names", "Error", "DataFrame"], correct_index=0, topic="Pandas 2", explanation="ngroups is count of groups."),
    QuizQuestion(question="What does df.groupby('col').indices return?", options=["Dict of group -> indices", "List", "Error", "DataFrame"], correct_index=0, topic="Pandas 2", explanation="indices maps group to index array."),
    QuizQuestion(question="What does pd.pivot_table(..., aggfunc='count') do?", options=["Counts per group", "Sums", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="aggfunc='count' counts values."),
    QuizQuestion(question="What does pd.pivot_table(..., aggfunc='sum') do?", options=["Sums per group", "Counts", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="aggfunc='sum' sums values."),
    QuizQuestion(question="What does pd.pivot_table(..., aggfunc='max') do?", options=["Max per group", "Min", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="aggfunc='max' takes maximum."),
    QuizQuestion(question="What does pd.pivot_table(..., aggfunc='min') do?", options=["Min per group", "Max", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="aggfunc='min' takes minimum."),
    QuizQuestion(question="What does pd.pivot_table(..., aggfunc=['mean','sum']) do?", options=["Multiple aggregations", "Single agg", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="List of aggfuncs applies multiple."),
    QuizQuestion(question="What does df.groupby('col').std() return?", options=["Std dev per group", "Single std", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="std() returns standard deviation per group."),
    QuizQuestion(question="What does df.groupby('col').var() return?", options=["Variance per group", "Single var", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="var() returns variance per group."),
    QuizQuestion(question="What does df.groupby('col').median() return?", options=["Median per group", "Single median", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="median() returns median per group."),
    QuizQuestion(question="What does df.groupby('col').quantile(0.5) return?", options=["50th percentile per group", "Single value", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="quantile() returns percentile per group."),
    QuizQuestion(question="What does df.groupby('col').cumsum() return?", options=["Cumulative sum per group", "Total sum", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="cumsum() gives running sum per group."),
    QuizQuestion(question="What does df.groupby('col').cummax() return?", options=["Cumulative max per group", "Total max", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="cummax() gives running max per group."),
    QuizQuestion(question="What does df.groupby('col').cummin() return?", options=["Cumulative min per group", "Total min", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="cummin() gives running min per group."),
    QuizQuestion(question="What does df.groupby('col').cumcount() return?", options=["Row number per group", "Count", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="cumcount() gives 0,1,2,... per group."),
    QuizQuestion(question="What does df.groupby('col').diff() return?", options=["Difference from previous per group", "Total diff", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="diff() gives difference from previous row."),
    QuizQuestion(question="What does df.groupby('col').pct_change() return?", options=["Pct change per group", "Total pct", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="pct_change() gives percent change."),
    QuizQuestion(question="What does df.groupby('col').rank() return?", options=["Rank per group", "Global rank", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="rank() ranks within each group."),
    QuizQuestion(question="What does df.groupby('col').shift(1) return?", options=["Shift down 1 per group", "Shift whole df", "Error", "Original df"], correct_index=0, topic="Pandas 2", explanation="shift() shifts values within group."),
    QuizQuestion(question="What does df.groupby('col').rolling(3) do?", options=["Rolling window per group", "Rolling whole df", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="rolling() creates rolling window per group."),
    QuizQuestion(question="What does df.groupby('col').expanding() do?", options=["Expanding window per group", "Expands df", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="expanding() creates expanding window."),
    QuizQuestion(question="What does df.groupby('col').agg({'a':'mean','b':'sum'}) do?", options=["Different agg per column", "Same agg", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="Dict specifies agg per column."),
    QuizQuestion(question="What does df.groupby('col').agg([np.mean, np.sum]) do?", options=["Multiple aggs per column", "Single agg", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="List applies multiple aggs."),
    QuizQuestion(question="What does df.groupby('col').agg('mean') do?", options=["Mean per group", "Single mean", "Error", "Nothing"], correct_index=0, topic="Pandas 2", explanation="String 'mean' applies mean."),
    QuizQuestion(question="What does df.groupby('col').agg(lambda x: x.max()-x.min()) do?", options=["Custom agg (range)", "Error", "Nothing", "Min only"], correct_index=0, topic="Pandas 2", explanation="Lambda applies custom function."),
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
    QuizQuestion(question="What does pd.merge(..., indicator=True) add?", options=["_merge column showing source", "Merge indicator", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="indicator=True adds _merge column."),
    QuizQuestion(question="What does pd.merge(..., validate='1:1') do?", options=["Checks 1:1 relationship", "Validates data", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="validate checks merge is 1:1."),
    QuizQuestion(question="What does pd.merge(..., validate='m:1') do?", options=["Checks many:1", "Checks 1:1", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="validate='m:1' checks many-to-one."),
    QuizQuestion(question="What does pd.merge(..., validate='1:m') do?", options=["Checks 1:many", "Checks many:1", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="validate='1:m' checks one-to-many."),
    QuizQuestion(question="What does pd.merge(..., validate='m:m') do?", options=["Checks many:many", "Checks 1:1", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="validate='m:m' checks many-to-many."),
    QuizQuestion(question="What does pd.concat(..., join='outer') do?", options=["Union of columns", "Intersection", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="join='outer' keeps all columns."),
    QuizQuestion(question="What does pd.concat(..., join='inner') do?", options=["Intersection of columns", "Union", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="join='inner' keeps common columns."),
    QuizQuestion(question="What does pd.concat(..., axis=0) do?", options=["Stack vertically (rows)", "Stack horizontally", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="axis=0 stacks along rows."),
    QuizQuestion(question="What does pd.concat(..., axis=1) do?", options=["Stack horizontally (columns)", "Stack vertically", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="axis=1 stacks along columns."),
    QuizQuestion(question="What does df1.merge(df2) use for keys?", options=["Common columns", "Index", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="merge uses common column names by default."),
    QuizQuestion(question="What does df1.join(df2, on='key') do?", options=["Joins on column key", "Joins on index", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="on= specifies join column."),
    QuizQuestion(question="What does pd.merge(..., sort=True) do?", options=["Sorts result by keys", "Sorts inputs", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="sort= sorts output by join keys."),
    QuizQuestion(question="What does pd.merge(..., copy=False) do?", options=["Avoid copy when possible", "No copy", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="copy=False can avoid copying."),
    QuizQuestion(question="What does pd.merge(..., left_index=True) do?", options=["Uses left index as key", "Uses right index", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="left_index=True uses left index."),
    QuizQuestion(question="What does pd.merge(..., right_index=True) do?", options=["Uses right index as key", "Uses left index", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="right_index=True uses right index."),
    QuizQuestion(question="What does pd.merge(..., how='cross') do?", options=["Cross join (Cartesian)", "Inner join", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="how='cross' creates Cartesian product."),
    QuizQuestion(question="What does df1.combine_first(df2) do?", options=["Fills nulls from df2", "Merges", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="combine_first fills nulls from df2."),
    QuizQuestion(question="What does df1.update(df2) do?", options=["Updates df1 in place from df2", "Returns new df", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="update() modifies df1 in place."),
    QuizQuestion(question="What does pd.merge(..., left_on='a', right_on='b') do?", options=["Joins on different column names", "Joins on same", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="left_on/right_on for different names."),
    QuizQuestion(question="What does pd.merge(..., on=['a','b']) do?", options=["Joins on multiple columns", "Joins on one", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="on= can be list of columns."),
    QuizQuestion(question="What does pd.concat(..., sort=True) do?", options=["Sorts columns", "Sorts rows", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="sort= sorts columns in result."),
    QuizQuestion(question="What does pd.concat(..., join_axes=...) do?", options=["Specify result axes (deprecated)", "Join axes", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="join_axes was for specifying axes."),
    QuizQuestion(question="What does df.align(other) return?", options=["(df1, df2) aligned", "Single df", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="align() aligns two DataFrames."),
    QuizQuestion(question="What does pd.merge(..., validate='one_to_one') do?", options=["Same as '1:1'", "Different", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="'one_to_one' is alias for '1:1'."),
    QuizQuestion(question="What does df1.append(df2) do?", options=["Appends rows (deprecated)", "Merges", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="append() is deprecated; use concat."),
    QuizQuestion(question="What does pd.concat(..., verify_integrity=True) do?", options=["Checks for duplicate index", "Verifies data", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="verify_integrity checks index uniqueness."),
    QuizQuestion(question="What does pd.merge(..., left_by=..., right_by=...) do?", options=["Grouped merge", "Simple merge", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="by= for grouped merge."),
    QuizQuestion(question="What does df.merge(..., suffixes=('_l','_r')) do?", options=["Conflict suffixes", "Add suffixes", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="suffixes= for overlapping columns."),
    QuizQuestion(question="What does pd.merge(..., how='left') keep?", options=["All left rows", "All right", "Matching only", "All"], correct_index=0, topic="Pandas 3", explanation="how='left' keeps all rows from left."),
    QuizQuestion(question="What does pd.merge(..., how='cross') do?", options=["Every row of left with every row of right", "Inner join", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="Cross join = Cartesian product."),
    QuizQuestion(question="What does df1.join(df2, how='outer') do?", options=["Outer join on index", "Inner join", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="how= specifies join type."),
    QuizQuestion(question="What does pd.concat(..., names=['x']) do?", options=["Names index levels", "Names columns", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="names= names index levels."),
    QuizQuestion(question="What does pd.merge(..., left_index=True, right_index=True) do?", options=["Join on index", "Join on columns", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="Both True = index join."),
    QuizQuestion(question="What does df.merge(..., how='inner') keep?", options=["Only matching rows", "All left", "All right", "All"], correct_index=0, topic="Pandas 3", explanation="how='inner' keeps only matches."),
    QuizQuestion(question="What does pd.concat(..., join='inner') do?", options=["Only common columns", "All columns", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="join='inner' keeps common columns."),
    QuizQuestion(question="What does df1.merge(df2, left_on='a', right_on='b') require?", options=["Both have specified columns", "Same names", "Error", "Nothing"], correct_index=0, topic="Pandas 3", explanation="Both must have the specified columns."),
    QuizQuestion(question="What does pd.merge(..., how='outer') keep?", options=["All rows from both", "Matching only", "Left only", "Right only"], correct_index=0, topic="Pandas 3", explanation="how='outer' keeps all rows."),
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
    QuizQuestion(question="What does oct(8) return?", options=["'8'", "'0o10'", "10", "Error"], correct_index=1, topic="Variables & DataTypes", explanation="oct() returns octal string."),
    QuizQuestion(question="What does bin(4) return?", options=["'4'", "'0b100'", "100", "Error"], correct_index=1, topic="Variables & DataTypes", explanation="bin() returns binary string."),
    QuizQuestion(question="What does complex(1, 0) return?", options=["1+0j", "1", "1.0", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="complex(real, imag) creates complex number."),
    QuizQuestion(question="What does bytes([65, 66]) return?", options=["b'AB'", "'AB'", "[65,66]", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="bytes() creates bytes from int list."),
    QuizQuestion(question="What does bytearray([1,2,3]) create?", options=["Mutable bytes", "Immutable bytes", "List", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="bytearray is mutable."),
    QuizQuestion(question="What does frozenset([1,2]) allow?", options=["add(3)", "Nothing - immutable", "discard(1)", "update"], correct_index=1, topic="Variables & DataTypes", explanation="frozenset is immutable."),
    QuizQuestion(question="What does (1,)*3 produce?", options=["(1, 1, 1)", "(1)", "Error", "(3)"], correct_index=0, topic="Variables & DataTypes", explanation="Tuple * n repeats."),
    QuizQuestion(question="What does 'x'.isdigit() return?", options=["True", "False", "Error", "0"], correct_index=1, topic="Variables & DataTypes", explanation="'x' is not a digit."),
    QuizQuestion(question="What does ' '.isspace() return?", options=["True", "False", "Error", "0"], correct_index=0, topic="Variables & DataTypes", explanation="Space is whitespace."),
    QuizQuestion(question="What does 'X'.isupper() return?", options=["True", "False", "Error", "1"], correct_index=0, topic="Variables & DataTypes", explanation="'X' is uppercase."),
    QuizQuestion(question="What does 'x'.islower() return?", options=["True", "False", "Error", "1"], correct_index=0, topic="Variables & DataTypes", explanation="'x' is lowercase."),
    QuizQuestion(question="What does 'Hi'.istitle() return?", options=["True", "False", "Error", "1"], correct_index=0, topic="Variables & DataTypes", explanation="'Hi' has title case."),
    QuizQuestion(question="What does 'hi'.capitalize() return?", options=["'Hi'", "'hi'", "'HI'", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="capitalize() uppercases first char."),
    QuizQuestion(question="What does 'HI'.casefold() return?", options=["'hi'", "'HI'", "'Hi'", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="casefold() for caseless comparison."),
    QuizQuestion(question="What does 'ab'.ljust(5) return?", options=["'ab   '", "'   ab'", "'ab'", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="ljust() pads on right."),
    QuizQuestion(question="What does 'ab'.rjust(5) return?", options=["'   ab'", "'ab   '", "'ab'", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="rjust() pads on left."),
    QuizQuestion(question="What does 'ab'.zfill(5) return?", options=["'000ab'", "'ab000'", "'ab'", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="zfill() pads with zeros on left."),
    QuizQuestion(question="What does 'a\tb'.expandtabs(4) do?", options=["Expands tabs to 4 spaces", "4 tabs", "Error", "Nothing"], correct_index=0, topic="Variables & DataTypes", explanation="expandtabs() replaces tabs."),
    QuizQuestion(question="What does 'hi'.encode() return?", options=["b'hi'", "'hi'", "Error", "None"], correct_index=0, topic="Variables & DataTypes", explanation="encode() converts to bytes."),
    QuizQuestion(question="What does b'hi'.decode() return?", options=["'hi'", "b'hi'", "Error", "None"], correct_index=0, topic="Variables & DataTypes", explanation="decode() converts bytes to str."),
    QuizQuestion(question="What does 'hi'.partition(' ') return?", options=["('hi','','')", "('hi',)", "Error", "['hi']"], correct_index=0, topic="Variables & DataTypes", explanation="partition splits at first sep."),
    QuizQuestion(question="What does 'a-b-c'.split('-', 1) return?", options=["['a','b-c']", "['a','b','c']", "Error", "['a']"], correct_index=0, topic="Variables & DataTypes", explanation="maxsplit=1 splits once."),
    QuizQuestion(question="What does '  hi  '.strip(' ') return?", options=["'hi'", "'  hi  '", "Error", "'hi '"], correct_index=0, topic="Variables & DataTypes", explanation="strip(' ') removes leading/trailing spaces."),
    QuizQuestion(question="What does 'abc'.lstrip('a') return?", options=["'bc'", "'abc'", "Error", "'ab'"], correct_index=0, topic="Variables & DataTypes", explanation="lstrip removes leading chars."),
    QuizQuestion(question="What does 'abc'.rstrip('c') return?", options=["'ab'", "'abc'", "Error", "'bc'"], correct_index=0, topic="Variables & DataTypes", explanation="rstrip removes trailing chars."),
    QuizQuestion(question="What does 'hi'.center(6) return?", options=["'  hi  '", "'hi'", "Error", "' hi '"], correct_index=0, topic="Variables & DataTypes", explanation="center() pads to center."),
    QuizQuestion(question="What does format(42, 'd') return?", options=["'42'", "42", "Error", "None"], correct_index=0, topic="Variables & DataTypes", explanation="format() with 'd' gives decimal string."),
    QuizQuestion(question="What does format(3.14, '.2f') return?", options=["'3.14'", "3.14", "Error", "None"], correct_index=0, topic="Variables & DataTypes", explanation="'.2f' = 2 decimal places."),
    QuizQuestion(question="What does '{0} {1}'.format('a','b') return?", options=["'a b'", "'0 1'", "Error", "'ab'"], correct_index=0, topic="Variables & DataTypes", explanation="format() substitutes by index."),
    QuizQuestion(question="What does '{x}'.format(x=5) return?", options=["'5'", "'x'", "Error", "5"], correct_index=0, topic="Variables & DataTypes", explanation="format() substitutes by name."),
    QuizQuestion(question="What does f'{1+1}' return?", options=["'2'", "'1+1'", "Error", "2"], correct_index=0, topic="Variables & DataTypes", explanation="f-string evaluates expression."),
    QuizQuestion(question="What does f'{x=}' return when x=3?", options=["'x=3'", "'3'", "Error", "3"], correct_index=0, topic="Variables & DataTypes", explanation="= in f-string adds name=value."),
    QuizQuestion(question="What does repr('hi') return?", options=["\"'hi'\"", "'hi'", "Error", "hi"], correct_index=0, topic="Variables & DataTypes", explanation="repr() gives string representation."),
    QuizQuestion(question="What does ascii('hi') return?", options=["'hi'", "'\\x68\\x69'", "Error", "hi"], correct_index=0, topic="Variables & DataTypes", explanation="ascii() escapes non-ASCII."),
    QuizQuestion(question="What does type(1) return?", options=["<class 'int'>", "int", "1", "Error"], correct_index=0, topic="Variables & DataTypes", explanation="type() returns the type object."),
    QuizQuestion(question="What does id(x) return?", options=["Unique integer for x", "Value of x", "Error", "None"], correct_index=0, topic="Variables & DataTypes", explanation="id() returns object identity."),
    QuizQuestion(question="What does hash((1,2)) return?", options=["Integer hash", "Error", "(1,2)", "None"], correct_index=0, topic="Variables & DataTypes", explanation="hash() returns hash value."),
    QuizQuestion(question="What does getattr(obj, 'x', 0) return?", options=["obj.x or 0 if missing", "obj.x only", "Error", "0"], correct_index=0, topic="Variables & DataTypes", explanation="getattr gets attr with default."),
    QuizQuestion(question="What does setattr(obj, 'x', 1) do?", options=["Sets obj.x = 1", "Gets obj.x", "Error", "Nothing"], correct_index=0, topic="Variables & DataTypes", explanation="setattr sets attribute."),
    QuizQuestion(question="What does delattr(obj, 'x') do?", options=["Deletes obj.x", "Sets to None", "Error", "Nothing"], correct_index=0, topic="Variables & DataTypes", explanation="delattr deletes attribute."),
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
