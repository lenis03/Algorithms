"""
    Consider a stack data structure. We have a function called remove_min tha
    t takes a stack as input and removes the smallest value from it.

    For instance:
    bottom [2, 8, 3, -6, 7, 3] top
    After applying remove_min(stack):
    bottom [2, 8, 3, 7, 3] top
"""
from typing import List


def remove_min(stack: List[int]):
    stack_storage = []

    if len(stack) == 0:  # if stack is empty
        return stack

    # Find the smallest value
    min = stack.pop()
    stack.append(min)
    for _ in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        stack_storage.append(val)

    # Back up stack and remove min value
    for _ in range(len(stack_storage)):
        val = stack_storage.pop()
        if val != min:
            stack.append(val)

    return stack, min


print(remove_min([2, 8, 3, -6, 7, 3]))
