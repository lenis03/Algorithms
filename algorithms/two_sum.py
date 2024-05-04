"""
    In this problem, we are required to find two numbers in an array whose sum
    equals a given target. To achieve this, we can iterate through the array
    and keep track of the elements we have seen so far in a hashmap.

    For each element `num` in the array, we check if `target - num` is already
    in the hashmap. If it is, we have found the two numbers that add up to the
    target.

    Finally, we return the indices of these two numbers. It is also mentioned
    that each input will have exactly one solution and the same element cannot
    be used twice.

    Now, let's implement this algorithm and find the indices of the
    two numbers that sum up to the target in the given example.
    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)

"""
from typing import List, Tuple


def two_sum(arry: List[int], target: int) -> Tuple[int, int] | None:
    result = dict()

    for i, num in enumerate(arry):

        if num in result:
            return result[num], i

        else:
            result[target - num] = i

    return None


print(two_sum([2, 7, 11, 15], 17))


def two_sum2(arry: List[int], target: int) -> Tuple[int, int] | None:
    f_index = 0
    l_index = len(arry) - 1

    while f_index < l_index:
        sum_t_num = arry[f_index] + arry[l_index]
        if sum_t_num == target:
            return f_index, l_index
        elif sum_t_num > target:
            l_index -= 1
        else:
            f_index += 1
