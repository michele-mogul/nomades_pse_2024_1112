def create_empty_dictionary():
    return {}

def add_key_value(dictionary, key, value):
    if isinstance(dictionary, dict):
        dictionary[key] = value
    pass

def get_value(dictionary, key):
    return dictionary[key] if key in dictionary else None

def check_key(dictionary, key):
    return key in dictionary

def remove_key_value(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        raise KeyError

def count_key_value_pairs(dictionary):
    return dictionary.__len__()

def get_keys(dictionary):
    if isinstance(dictionary, dict):
        return list(dictionary.keys())
    return None

def get_values(dictionary):
    if isinstance(dictionary, dict):
        return list(dictionary.values())
    return None

def get_items(dictionary):
    if isinstance(dictionary, dict):
        return list(dictionary.items())
    return None

def update_values(dictionary, key, value):
    if isinstance(dictionary, dict) and key in dictionary:
        dictionary[key] = value
    pass

def merge_dictionaries(dictionary1, dictionary2):
    if isinstance(dictionary1, dict) and isinstance(dictionary2, dict):
        return {**dictionary1, **dictionary2}
    return None

def clear_dictionary(dictionary):
    if isinstance(dictionary, dict):
        dictionary.clear()
    pass

def find_key_with_max_value(dictionary):
    if isinstance(dictionary, dict):
        return max(dictionary, key=dictionary.get)
    return None

def find_key_with_min_value(dictionary):
    if isinstance(dictionary, dict):
        return min(dictionary, key=dictionary.get)
    return None

def check_same_key_value_pairs(dictionary1, dictionary2):
    if isinstance(dictionary1, dict) and isinstance(dictionary2, dict):
        return dictionary1.items() == dictionary2.items()
    return False
