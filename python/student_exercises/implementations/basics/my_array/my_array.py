import builtins

import numpy
import numpy as np


def sort_ascending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in ascending order 
    :param arr: the array to sort
    :return: the sorted array in ascending order
    """
    arr.sort()
    return arr

def sort_descending(arr: list[int]) -> list[int]:
    """
    Function that returns the sorted array in descending order 
    :param arr: the array to sort
    :return: the sorted array in descending order
    """
    arr.sort(reverse=True)
    return arr

def sum(tableau: list[int]) -> int:
    """
    Function that returns the sum of the elements of the array
    :param tableau: the array to sum
    :return: the sum of the elements of the array
    """
    i_sum = 0
    for i in tableau:
        i_sum += i
    return i_sum


def average(tableau: list[int]) -> float:
    """
    Function that returns the average of the elements of the array
    :param tableau: the array to average
    :return: the average of the elements of the array
    """
    return sum(tableau) / len(tableau)


def min(tableau: list[int]) -> int:
    """
    Function that returns the minimum of the elements of the array
    :param tableau: the array to find the minimum of
    :return: the minimum of the elements of the array
    """
    i_min_value = tableau[0]
    for i in tableau:
        if i < i_min_value:
            i_min_value = i
    return i_min_value


def max(tableau: list[int]) -> int:
    """
    Function that returns the maximum of the elements of the array
    :param tableau: the array to find the maximum of
    :return: the maximum of the elements of the array
    """
    i_max_value = tableau[0]
    for i in tableau:
        if i > i_max_value:
            i_max_value = i
    return i_max_value


def min_max(tableau: list[int]) -> tuple[int, int]:
    """
    Function that returns the minimum and maximum of the elements of the array
    :param tableau: the array to find the minimum and maximum of
    :return: the minimum and maximum of the elements of the array
    """

    return [min(tableau), max(tableau)]


def median(tableau: list[int]) -> float | int:
    """
    Function that returns the median of the elements of the array
    :param tableau: the array to find the median of
    :return: the median of the elements of the array
    """
    tableau.sort()
    if len(tableau) % 2 == 0:
        return (tableau[len(tableau) // 2 - 1] + tableau[len(tableau) // 2]) / 2
    else:
        return tableau[len(tableau) // 2]


def mode(tableau: list[int]) -> int:
    """
    Function that returns the mode of the elements of the array
    The mode is the value that appears most often in a set of data values.
    If there is a tie, the mode is the smallest value.
    :param tableau: the array to find the mode of
    :return: the mode of the elements of the array
    """
    d_count, i_mode = {}, tableau[0]
    for i_index, i_value in enumerate(tableau):
        if d_count.get(i_value) is None:
            d_count[i_value] = 0

        d_count[i_value] = d_count.get(i_value, 0) + 1
        if d_count[i_value] > d_count[i_mode]:
            i_mode = tableau[i_index]

    return i_mode

def variance(tableau: list[int]) -> float:
    """
    Function that returns the variance of the elements of the array
    :param tableau: the array to find the variance of
    :return: the variance of the elements of the array
    """
    m = builtins.sum(tableau) / len(tableau)
    var = builtins.sum((x - m) ** 2 for x in tableau) / len(tableau)
    return var
        
    

def standard_deviation(tableau: list[int]) -> float:
    """
    Function that returns the standard deviation of the elements of the array
    The standard deviation is the square root of the variance.
    :param tableau: the array to find the standard deviation of
    :return: the standard deviation of the elements of the array
    """
    return variance(tableau) ** 0.5


def exist(tableau: list[int], valeur: int) -> bool:
    """
    Function that returns True if the value exists in the array
    :param tableau: the array to check if the value exists in
    :param valeur: the value to check if it exists in the array
    :return: True if the value exists in the array, False otherwise
    """
    return valeur in tableau


def position(tableau: list[int], valeur: int) -> int:
    """
    Function that returns the position of the first value in the array
    If the value does not exist in the array, it returns -1
    :param tableau: the array to find the position of
    :param valeur: the value to find the position of
    :return: the position of the value in the array
    """
    if valeur in tableau:
        return tableau.index(valeur)
    return -1


def similars(arr1: list[int], arr2: list[int]) -> bool:
    """
    Function that returns True if the two arrays are similar
    :param arr1: the first array
    :param arr2: the second array
    :return: True if the two arrays are similar, False otherwise
    """
    return arr1 == arr2


def is_list(tableau) -> bool:
    """
    Function that returns True if the array is a table
    :param tableau: the array to check if it is a table
    :return: True if the array is a table, False otherwise
    """

    return isinstance(tableau, list)


def is_list_of_numbers(tableau) -> bool:
    """
    Function that returns True if the array is a table of numbers
    :param tableau: the array to check if it is a table of numbers
    :return: True if the array is a table of numbers, False otherwise
    """
    return (is_list(tableau) and len(tableau) > 0
            and (all(isinstance(x, int)
                 or isinstance(x, float)
                 or isinstance(x, complex)
                 for x in tableau))
            )
