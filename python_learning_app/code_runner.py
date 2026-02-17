"""
Restricted code execution for the coding section.
Blocks: classes, files, databases (per user preference).
"""
import re


# Patterns that are not allowed in user code
BLOCKED_PATTERNS = [
    r"\bclass\s+\w+",           # class definitions
    r"\bopen\s*\(",             # open()
    r"\b__import__\s*\(",       # __import__
    r"\bimport\s+(os|io|pathlib|sqlite3|dbm|shelve|pickle)\b",
    r"\bfrom\s+(os|io|pathlib|sqlite3|dbm|shelve|pickle)\s+import",
    r"\.read\s*\(",             # file read
    r"\.write\s*\(",            # file write
    r"\.read_excel\s*\(",       # pandas read_excel
    r"\.read_csv\s*\(",         # pandas read_csv (could load from file)
    r"pd\.read_",               # pandas file readers
    r"exec\s*\(",               # exec()
    r"eval\s*\(",               # eval() - can be dangerous
    r"compile\s*\(",
    r"__builtins__",
    r"globals\s*\(",
    r"locals\s*\(",
]


def is_code_allowed(code: str) -> tuple[bool, str]:
    """
    Check if user code is allowed (no classes, files, databases).
    Returns (allowed: bool, reason: str).
    """
    if not code or not code.strip():
        return False, "Code is empty."
    
    code_lower = code.lower()
    
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, code, re.IGNORECASE):
            if "class" in pattern:
                return False, "Classes are not allowed in the coding section."
            if "open" in pattern or "read" in pattern or "write" in pattern or "read_excel" in pattern or "read_csv" in pattern or "pd.read" in pattern:
                return False, "File operations are not allowed in the coding section."
            if "sqlite" in pattern or "dbm" in pattern or "shelve" in pattern:
                return False, "Database operations are not allowed in the coding section."
            if "import" in pattern and any(x in pattern for x in ["os", "io", "pathlib"]):
                return False, "File-related imports are not allowed."
            if "exec" in pattern or "eval" in pattern:
                return False, "exec() and eval() are not allowed for security."
    
    return True, ""


def run_restricted_code(code: str) -> tuple[bool, str, str]:
    """
    Run code in a restricted environment.
    Returns (success: bool, output: str, error: str).
    """
    allowed, reason = is_code_allowed(code)
    if not allowed:
        return False, "", reason
    
    import io
    import sys
    
    old_stdout = sys.stdout
    sys.stdout = captured = io.StringIO()
    
    try:
        safe_globals = {
            "__builtins__": __builtins__,
            "print": print,
            "len": len,
            "range": range,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "round": round,
            "sorted": sorted,
            "reversed": reversed,
            "enumerate": enumerate,
            "zip": zip,
            "map": map,
            "filter": filter,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "type": type,
            "isinstance": isinstance,
            "True": True,
            "False": False,
            "None": None,
        }
        exec(code, safe_globals)
        output = captured.getvalue()
        return True, output, ""
    except Exception as e:
        return False, captured.getvalue(), str(e)
    finally:
        sys.stdout = old_stdout


def explain_error(error_msg: str) -> str:
    """Convert Python error messages into clear, simple explanations."""
    err = error_msg.lower()
    if "nameerror" in err and "is not defined" in err:
        # Extract variable name if possible
        import re
        m = re.search(r"name '([^']+)' is not defined", error_msg, re.I)
        var = m.group(1) if m else "a variable"
        return f"**Variable not defined:** You used '{var}' before giving it a value. Assign a value first, e.g. `{var} = 5`"
    if "syntaxerror" in err:
        return "**Syntax error:** Check for missing colons (`:`), parentheses `()`, brackets `[]`, or quotes. Make sure every opening symbol has a matching closing one."
    if "indentationerror" in err:
        return "**Indentation error:** Python uses spaces to group code. Lines that belong together (e.g. inside a loop) must be indented the same way. Use 4 spaces."
    if "typeerror" in err and "unsupported operand" in err:
        return "**Type error:** You're mixing incompatible types. For example, you can't add a string and a number. Use `str()` or `int()` to convert."
    if "indexerror" in err and "out of range" in err:
        return "**Index error:** You're accessing a position that doesn't exist in the list. Remember: the first item is at index 0, and the last is at `len(list)-1`."
    if "keyerror" in err:
        return "**Key error:** You're trying to access a key that doesn't exist in the dictionary. Use `.get()` for a safe default, or check if the key exists first."
    if "zerodivisionerror" in err:
        return "**Division by zero:** You can't divide by zero. Check that your divisor isn't 0."
    if "valueerror" in err:
        return "**Value error:** The value you're using isn't valid for this operation. For example, `int('hello')` fails because 'hello' isn't a number."
    if "attributeerror" in err and "'nonetype'" in err:
        return "**NoneType error:** You're calling a method on `None`. A function might have returned `None` instead of a value. Check your function's return statement."
    if "attributeerror" in err:
        return "**Attribute error:** You're trying to use a method or property that doesn't exist for this type. Check the spelling and that you're using the right type."
    # Default: show original with a friendly intro
    return f"**Error:** {error_msg}"
