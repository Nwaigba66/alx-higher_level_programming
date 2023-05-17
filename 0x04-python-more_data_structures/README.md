# Python - More Data Structures: Set, Dictionary

## General
### What are sets and how to use them?
-  set is a data structure that represents a collection of unique elements in no particular order.
   Sets are commonly used to efficiently store and manipulate distinct values and
   perform set operations such as union, intersection, and difference.

### What are the most common methods of set and how to use them?
### Here are some of the most common methods available for sets:

- add(element): Adds an element to the set if it is not already present.
  If the element is already in the set, it won't be added again.
- remove(element): Removes an element from the set. If the element is not found, it raises a KeyError.
- discard(element): Removes an element from the set if it is present. If the element is not found, it does nothing.
- pop(): Removes and returns an arbitrary element from the set. Since sets are unordered, the element returned is not predictable.
- clear(): Removes all elements from the set, making it empty.
- copy(): Returns a shallow copy of the set.

### How to iterate into a set?
- In Python, you can use a for loop to iterate over a set. Since sets are unordered, 
  the order of iteration is not guaranteed.

### For this projects we will use the following files and functions:
- 0-square_matrix_simple.py - function that computes the square value of all integers of a matrix.
- 1-search_replace.py - function that replaces all occurrences of an element by another in a new list.
- 2-uniq_add.py - function that adds all unique integers in a list (only once for each integer).
- 3-common_elements.py - function that returns a set of common elements in two sets.
- 4-only_diff_elements.py - function that returns a set of all elements present in only one set.
- 5-number_keys.py - function that returns the number of keys in a dictionary.
- 6-print_sorted_dictionary.py - function that prints a dictionary by ordered keys.
- 7-update_dictionary.py - function that replaces or adds key/value in a dictionary.
- 8-simple_delete.py - function that deletes a key in a dictionary.
- 9-multiply_by_2.py - function that returns a new dictionary with all values multiplied by 2.
- 10-best_score.py - function that returns a key with the biggest integer value.
- 11-multiply_list_map.py -  function that returns a list with all values multiplied by a number without using any loops.
- 12-roman_to_int.py

