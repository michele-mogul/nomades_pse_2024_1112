def get_first_three_elements(lst):
    if isinstance(lst, list):
        return lst[:3]
    return None

def get_last_two_elements(lst):
    if isinstance(lst, list):
        return lst[-2:]
    return None

def reverse_list(lst):
    if isinstance(lst, list):
        return lst[::-1]
    return None

def get_even_index_elements(lst):
    if isinstance(lst, list):
        return lst[::2]
    return None

def get_odd_index_elements(lst):
    if isinstance(lst, list):
        return lst[1::2]
    return None

def remove_duplicates(lst):
    if isinstance(lst, list):
        return list(set(lst))
    return None

def square_elements(lst):
    if isinstance(lst, list):
        return [x**2 for x in lst]
    return None

def double_elements(lst):
    if isinstance(lst, list):
        return [x*2 for x in lst]
    return None

def sum_of_elements(lst):
    if isinstance(lst, list):
        return sum(lst)
    return None

def is_sorted(lst):
    if isinstance(lst, list):
        return sorted(lst) == lst
    return None

def count_occurrences(lst, element):
    if isinstance(lst, list):
        return lst.count(element)
    return None

def find_maximum(lst):
    if isinstance(lst, list) and len(lst) > 0:
        return max(lst)
    return None

def find_minimum(lst):
    if isinstance(lst, list) and len(lst) > 0:
        return min(lst)
    return None

def combine_lists(lst1, lst2):
    if isinstance(lst1, list) and isinstance(lst2, list) :
        if len(lst1) == 0:
            return lst2[:]
        elif len(lst2) == 0:
            return lst1[:]
        else:
            result = [None] * (len(lst1) + len(lst2))
            result[::2] = lst1
            result[1::2] = lst2
            return result
    return None

def is_palindrome(lst):
    if isinstance(lst, list):
        return lst == lst[::-1]
    return None
