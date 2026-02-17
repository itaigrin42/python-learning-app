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
