from typing import List, Tuple
from random import randint


class OneTimePad:

    @staticmethod
    def encrypt(text: str) -> Tuple[List[int], List[int]]:
        """
        Function to encrypt text using pseudo-random numbers
        >>> OneTimePad().encrypt("")
        ([], [])
        >>> OneTimePad().encrypt([])
        ([], [])
        >>> random.seed(1)
        >>> OneTimePad().encrypt(" ")
        ([6969], [69])
        >>> random.seed(1)
        >>> OneTimePad().encrypt("Hello")
        ([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
        >>> OneTimePad().encrypt(1)
        Traceback (most recent call last):
        ...
        TypeError: 'int' object is not iterable
        >>> OneTimePad().encrypt(1.1)
        Traceback (most recent call last):
        ...
        TypeError: 'float' object is not iterable
        """
        cipher = []
        key = []

        plain_unicode = [ord(i) for i in text]

        for i in plain_unicode:
            k = randint(1, 1000)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)

        return cipher, key

    @staticmethod
    def decrypt(cipher: List[int], key: List[int]) -> str:
        """
        Function to decrypt text using pseudo-random numbers.
        >>> OneTimePad().decrypt([], [])
        ''
        >>> OnepaTimePad.decrypt([35], [])
        ''
        >>> OneTimePad().decrypt([], [35])
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        >>> random.seed(1)
        >>> OneTimePad().decrypt([9729, 114756, 4653, 31309, 10492], [69, 292, 33, 131, 61])
        'Hello'
        """
        plain = []
        for i in range(len(key)):
            plain_unicode = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(plain_unicode))

        result = ''.join([i for i in plain])

        return result
