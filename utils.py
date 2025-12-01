def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return a + b


def reverse_string(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text[::-1]
