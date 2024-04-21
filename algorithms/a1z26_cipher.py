"""
    Convert a string of characters to a sequence of numbers corresponding to
    the character's position in the alphabet.

    This process involves converting each letter in a given string to it's
    corresponding numerical position in the English alphabet. For example,
    'A' would be 1, 'B' would be 2, and so on.

    You can find more information and tools to perform this conversion using
    the following links:

    - [Letter Number Cipher Tool](https://www.dcode.fr/letter-number-cipher)
    - [A1Z26 Cipher Tool](http://bestcodes.weebly.com/a1z26.html)


"""
from typing import List


def encode(plain: str) -> List[int]:
    """
    >>> encode("Fardin")
    [37, 64, 81, 67, 72, 77]
    """
    return [ord(elem) - 33 for elem in plain]


def decode(encode: List[int]) -> str:
    """
    >>> decode([37, 64, 81, 67, 72, 77])
    "Fardin"
    """
    return "".join((chr(elem + 33) for elem in encode))
