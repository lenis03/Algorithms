"""
    **Algorithm : ZIGZAG ITERATOR**
    The Zigzag Iterator algorithm takes two lists and iterates through them in
    a zigzag manner, alternating between elements from each list. For example,
    given the input lists [1, 3, 5, 7, 9] and [2, 4, 6, 8, 10], the
    Zigzag Iterator would output the elements in the
    following order: 1 2 3 4 5 6 7 8 9 10.
"""
from typing import List


class ZigZagIterator:

    def __init__(self, l1: List[int], l2: List[int]) -> None:
        self.queue: List[List[int]] = [l1, l2]

    def next(self) -> int:
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

    def has_next(self) -> bool:
        if self.queue:
            return True
        return False


l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]

z = ZigZagIterator(l1, l2)

while z.has_next():
    print(z.next(), end=' ')
