def create_empty_tuple():
    return ()

def create_tuple_from_list(lst):
    return tuple(lst)

def access_element(t, index):
    return t[index]

def slice_tuple(t, start, end):
    return t[start:end]

def check_element(t, element):
    return element in t

def get_tuple_length(t):
    return len(t)

def concatenate_tuples(t1, t2):
    return t1 + t2

def count_occurrences(t, element):
    return t.count(element)

def find_index(t, element):
    return t.index(element)

def check_equal(t1, t2):
    return t1 == t2

def find_maximum(t):
    return max(t)

def find_minimum(t):
    return min(t)

def convert_tuple_to_list(t):
    return list(t)

def convert_list_to_tuple(lst):
    return tuple(lst)

def sort_tuple(t):
    return tuple(sorted(t))
