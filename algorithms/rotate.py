"""
    Rotation: Rotating a string means shifting its characters to the right, with characters wrapping around from the end to the beginning.
    Positive k:  The value of `k` will always be a positive integer.

    Examples:

    rotate("hello", 2) returns "llohe"
    rotate("hello", 5) returns "hello"
    rotate("hello", 6) returns "elloh"
    rotate("hello", 7) returns "llohe"
    rotate("hello", 102) returns "lohel"

""" 

def rotate(s: str, k: int):
    dubble_str = s + s
    
    if k < len(s):
        return dubble_str[k: len(s) + k]

    else:
        return dubble_str[k - len(s): k]
