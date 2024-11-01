def create_empty_set():
    return set()

def create_set_from_list(lst):
    return set(lst)

def add_element(s, element):
    if isinstance(s, set):
        s.add(element)
    pass

def remove_element(s, element):
    if isinstance(s, set) and element in s:
        s.remove(element)
    else:
        raise KeyError

def check_element(s, element):
    return isinstance(s, set) and element in s

def count_elements(s):
    return len(s)

def union_sets(s1, s2):
    if isinstance(s1, set) and isinstance(s2, set):
        return s1.union(s2)
    return None

def intersect_sets(s1, s2):
    if isinstance(s1, set) and isinstance(s2, set):
        return s1.intersection(s2)
    return None

def difference_sets(s1, s2):
    if isinstance(s1, set) and isinstance(s2, set):
        return s1.difference(s2)
    return None

def check_subset(s1, s2):
    if isinstance(s1, set) and isinstance(s2, set):
        return s1.issubset(s2)
    return None

def check_disjoint(s1, s2):
    if isinstance(s1, set) and isinstance(s2, set):
        return s1.isdisjoint(s2)
    return None

def clear_set(s):
    if isinstance(s, set):
        s.clear()
    pass

def copy_set(s):
    if isinstance(s, set):
        return s.copy()
    return None

def find_maximum(s):
    if isinstance(s, set):
        return max(s)
    return None

def check_equal(s1, s2):
    return s1 == s2
