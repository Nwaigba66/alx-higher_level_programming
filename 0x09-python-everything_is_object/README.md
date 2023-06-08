# Python - Everything is object

# How to display the variable identifier (which is the memory address in the CPython implementation)?
- In Python, you can display the memory address or identifier of an object using the built-in id() function.
 The id() function returns a unique identifier for an object, which represents its memory address in the CPython implementation.

# What is mutable and immutable?
- In Python, objects can be classified as either mutable or immutable based on whether their state can be changed after they are created.

An immutable object is an object whose state cannot be modified after it is created. Immutable objects in Python include built-in types like integers, floats, strings, and tuples. Once an immutable object is created, any operation that appears to modify its state actually creates a new object with the updated value. Immutable objects are hashable and can be used as keys in dictionaries.

# What are the built-in mutable types?
- In Python, there are several built-in mutable types that allow for modifications to their internal state after they are created.
 These mutable types include:

- List (list): Lists are ordered collections of items, and they can be modified by adding, removing, or changing elements. Lists are created using square brackets [ ] or the list() constructor.

- Dictionary (dict): Dictionaries are key-value pairs where each value is associated with a unique key. They can be modified by adding, updating, or deleting key-value pairs. Dictionaries are created using curly braces { } or the dict() constructor.

- Set (set): Sets are unordered collections of unique elements. They can be modified by adding or removing elements. Sets are created using curly braces { } or the set() constructor.

- Byte array (bytearray): Byte arrays are mutable sequences of bytes. They can be modified by changing the values of individual bytes. Byte arrays are created using the bytearray() constructor.
