"""
    Bead sort, also known as gravity sort, is an interesting sorting algorithm
    that operates specifically on sequences of non-negative integers. It is a
    unique sorting technique that differs from traditional comparison-based
    sorting algorithms like quicksort or mergesort.

    In Bead sort, each element in the sequence is represented by beads.
    These beads can be imagined as small, colored balls that slide
    along vertical rods. The beads are initially placed at the
    top of the rods, with the number of beads representing
    the value of the corresponding element.

    The sorting process works by allowing the beads to fall under the force of
    gravity. As the beads fall, they accumulate at the bottom of the rods,
    forming the sorted sequence from lowest to highest value. The efficiency
    and simplicity of Bead sort make it an interesting
    algorithm to study and explore.

    For more detailed information and a thorough explanation of how Bead sort
    works, you can refer to the official Wikipedia page on Bead sort at the
    following link: [Bead Sort - Wikipedia](https://en.wikipedia.org/wiki/Bead_sort)
    [6, 11, 12, 4, 1, 5]   ==>   [1, 4, 5, 6, 11, 12]

"""
from typing import List


def bead_sort(sequence: List[int]) -> List[int]:
    """
    >>> bead_sort([6, 11, 12, 4, 1, 5])
    [1, 4, 5, 6, 11, 12]

    >>> bead_sort([9, 8, 7, 6, 5, 4 ,3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> bead_sort([5, 0, 4, 3])
    [0, 3, 4, 5]

    >>> bead_sort([8, 2, 1])
    [1, 2, 8]

    >>> bead_sort([1, .9, 0.0, 0, -1, -.9])
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers

    >>> bead_sort("Hello world")
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers
    """

    if any(not isinstance(i, int) or i < 0 for i in sequence):
        raise TypeError("Sequence must be list of non-negative integers")

    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i+1] += rod_upper - rod_lower

    return sequence
