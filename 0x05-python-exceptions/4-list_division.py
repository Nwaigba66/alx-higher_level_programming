#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                try:
                    division_result = element_1 / element_2
                    result.append(division_result)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)
            else:
                print("wrong type")
                result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    
    return result
