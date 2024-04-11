"""
    Julius Caesar protected his sensitive information by encrypting it using
    a cipher known as Caesar's cipher. This method shifts each letter
    by a specific number of positions. If the shift extends beyond 
    the alphabet's end, it wraps around back to the beginning.
    For instance, with a shift of 3, letters w, x, y, and z would correspond
    to z, a, b, and c.

    Original alphabet: abcdefghijklmnopqrstuvwxyz Alphabet shifted by +3:
    defghijklmnopqrstuvwxyzabc

    By employing this simple yet effective technique,
    Caesar managed to encode his communications and safeguard confidential
    data from unauthorized access.
"""

from string import ascii_letters
from typing import Dict


def caesar_cipher(string: str, key: int, alphabet: str | None = None) -> str:
    """
    Encodes a given string with the caesar cipher and returns the encoded
    """

    alpha = alphabet or ascii_letters
    result = ''

    for char in string:
        if char not in alpha:
            result += char
        else:
            new_key = (alpha.index(char) + key) % len(alpha)
            result += alpha[new_key]

    return result


def decrypt(string: str, key: int, alphabet: str | None = None) -> str:
    """
    Decodes a given string of cipher-text and returns the decoded plain-text
    """

    key *= -1
    return caesar_cipher(string, key)


def brute_force(string: str, alphabet: str | None = None) -> Dict[str, int]:
    """
    Returns all the possible combinations of keys and the decoded strings in the
    form of a dictionary
    """
    alpha = alphabet or ascii_letters
    key = 1
    result = {}

    while key <= len(alpha):
        result[key] = decrypt(string, key, alphabet)
        key += 1

    return result
