from /Users/takiuddinahmed/Downloads/test_output_replacement.py import compile_restricted
from RestrictedPython import safe_globals

def process_code(code):
    """
    Executes a user-defined Python function in a restricted environment.

    Args:
    - code (str): Python code containing a function definition.

    Returns:
    - Any: Output of the user-defined function.
    """
    loc = {"return": None}
    byte_code = compile_restricted(code, '<inline>', 'exec')
    exec(byte_code, safe_globals, loc)

    # Execute the main function and store its result under the 'return' key
    loc["return"] = loc['main']()

    # Return the result
    return loc["return"]

code_sample = """
def main():
    a = 1
    b = 2

    return (a + b) * 2
"""

output = process_code(code_sample)


print(output)
