## Python Algorithms

This repository contains a collection of commonly used algorithms implemented in Python.

### Algorithms Included:

- **Limit**: Find the minimum value of a given list of numbers.
- **Top One**: Find the largest value in a given list of numbers.
- **Caesar Cipher**: Encrypt a message using the Caesar cipher.
- **Search Insert**: Find the position where an element should be inserted in a sorted list.
- **Is Isomorphic**: Check if two strings are isomorphic.
- **A1Z26 Cipher**: Encrypt a message using the A1Z26 cipher.
- **Bead Sort**: Sort a list of numbers using the bead sort algorithm.
- **Zig Zag Iterator**: Create an iterator that traverses a matrix in a zig-zag pattern.
- **Move Zeros**: Move all zeros to the end of a given list.
- **Remove Min**: Remove the minimum value from a given list.
- **OneTimePad Cipher**: Encrypt a message using the OneTimePad cipher.
- **Two Sum**: Find two numbers in a given list that sum to a given target value.
- **Rotate**: Rotate a list by a given number of positions.
- **Search Range**: Find the first and last occurrences of an element in a sorted list.
- **Linear Search**: Perform a linear search for a given element in a list.
- **Binary Search**: Perform a binary search for a given element in a sorted list.
- **First Occurrence**: Find the first occurrence of an element in a given list.
- **Last Occurrence**: Find the last occurrence of an element in a given list.
- **Chunked**: Split a list into evenly sized chunks.
- **First**: Retrieve the first element from a list.
- **Last**: Retrieve the last element from a list.
- **Nth or Last**: Retrieve the nth element or the last element if n is out of range.
- **One**: Ensure a list contains exactly one element.
- **Interleave**: Interleave multiple lists into one list.
- **Repeat Each**: Repeat each element in a list a given number of times.
- **Strictly N**: Check if a list contains exactly n elements.
- **Only**: Ensure a list contains only one unique element.
- **Always Reversible**: Ensure a list is always reversible.
- **Always Iterable**: Ensure an object is always iterable.
- **Split After**: Split a list after every n elements.
- **Split Into**: Split a list into n parts.
- **Map If**: Conditionally apply a function to elements in a list.
- **Time Limited**: Limit the execution time of a function.
- **Difference**: Find the difference between two lists.
- **Value Chain**: Chain multiple lists into a single list.
- **Sequence View**: Provide a view into a sequence with start and end positions.

### Usage

To use any of the algorithms, simply import the corresponding module and call the appropriate function. For example:

```python
from algorithms.limit import limit

result = limit([1, 2, 3, 4, 5])
print(result)

For new algorithms, you can use them in a similar way:

python
from algorithms.more import chunked, first

chunked_result = chunked([1, 2, 3, 4, 5], 2)
print(chunked_result)

first_element = first([1, 2, 3, 4, 5])
print(first_element)
```

### Testing

The tests for each algorithm are included in the `test_more.py` file. You can run the tests to ensure everything is working correctly. For example:



```bash
python -m unittest test_more.py
```
### Or
You can use pytest package:
```bash
pytest test_more.py
```
