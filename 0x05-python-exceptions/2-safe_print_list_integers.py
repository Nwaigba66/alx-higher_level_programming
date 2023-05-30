#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        iterator = iter(my_list)
        while count < x:
            try:
                element = next(iterator)
                if isinstance(element, int):
                    print("{:d}".format(element), end=" ")
                    count += 1
            except IndexError:
                break
    except StopIteration:
        pass
    print()
    return (count)
