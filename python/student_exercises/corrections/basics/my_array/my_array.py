def sort_ascending(arr: list[int]) -> list[int]: # O(n^2)
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    def find_index_of_minimum(values: list[int]) -> int:
        minimum_value = values[0]
        minimum_value_index = 0
        for index, value in enumerate(values):
            if value < minimum_value:
                minimum_value = value
                minimum_value_index = index
        return minimum_value_index
    
    unsorted_array = arr.copy()
    sorted_array = []

    while len(unsorted_array) > 0:
        minimum = unsorted_array.pop(find_index_of_minimum(unsorted_array))
        sorted_array.append(minimum)

    return sorted_array


def sort_descending(arr: list[int]) -> list[int]: # O(n^2)
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    arr_2 = arr.copy()                                        # O(1)
    for i in range(len(arr_2)):                               # O(n^2)
        for j in range(i+1, len(arr_2)):                    # O(n)
            if arr_2[i] < arr_2[j]:                       # O(1)
                arr_2[i], arr_2[j] = arr_2[j], arr_2[i]   # O(1)
            
    return arr_2

def sum(tableau: list[int]) -> int: # O(n)
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    sum_ = 0                       # O(1)
    # for element in tableau:
    #   total += element

    for i in range(len(tableau)): # O(n)
        sum_ += tableau[i]        # O(1)
    return sum_                   # O(1)

def average(tableau: list[int]) -> float: # O(n)
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    # total = 0
    # n = len(tableau)

    # for i in tableau:
    #   total += i

    # return total/n

    return sum(tableau) / len(tableau) # O(n)
 

def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array

    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    minimum=tableau[0]
    for element in tableau[1:]:
        if element<minimum:
            minimum = element
    return minimum


def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """    
    max_=tableau[0]
    for element in tableau[1:]:
        if element > max_:
            max_ = element
    return max_


def min_max(tableau: list[int]) -> tuple[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """
    return min(tableau), max(tableau)


def median(tableau: list[int]) -> int | float:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    arr = sort_ascending(tableau)
    mid = len(arr) // 2
    if len(arr)%2==1:
        return arr[mid]

    return (arr[mid-1]+arr[mid]) / 2  
    # return arr[mid] if len(arr)%2==1 else (arr[mid-1]+arr[mid]) / 2


def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements of the array
    """
    return None

def variance(tableau: list[int]) -> float: # O(n)
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    sum_ = 0                                      # O(1)
    avg = average(tableau)                        # O(n)
    for element in tableau:                       # O(n)
        sum_ += (element-avg)**2  # O(1)
    return sum_ / len(tableau)                    # O(1)
    

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    # import math
    # return math.sqrt(variance(tableau))
    return variance(tableau) ** (1/2)


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    # for element in tableau:
    #     if element == valeur:
    #         return True
    # return False
    return valeur in tableau


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    # for i in range(len(tableau)):
    #     if tableau[i] == valeur:
    #         return i
    # return -1

    for idx, val in enumerate(tableau):
        if valeur == val:
            return idx
    return -1


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    # if len(arr1) != len(arr2):
    #     return False

    # for i in range(len(arr1)):
    #     if arr1[i] != arr2[i]:
    #         return False
    # return True

    return arr1 == arr2


def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """
    return None


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    return None