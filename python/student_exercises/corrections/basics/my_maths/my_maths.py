def is_even(number: int) -> str: # O(1)
    """
    Function that checks if a number is even or odd.
    Return the string "The number is even" if the number is even, "The number is odd" otherwise.
    params:
      number: The number to check
    
    Returns:
      A string that says if the number is even or odd
    """
    # if number % 2 == 0:
    #    return "The number is even"

    # return "The number is odd"
    return "The number is even" if number % 2 == 0 else "The number is odd"

        

def factorial(n: int) -> int: # O(n)
    """
    Function that computes the factorial of a number.
    The factorial of n is the product of all positive integers less than or equal to n.
    :param n: The number to compute the factorial of
    :return: The factorial of n
    """
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def fact_for(n):
    ret = 1
    for ni in range(n, 0, -1):
        ret *= ni
    return ret

def fibonacci(n: int) -> int: # O(2^n) | O(n)
    """
    Function that computes the nth Fibonacci number.
    :param n: The index of the Fibonacci number to compute
    :return: The nth Fibonacci number
    """
    # if n == 0 or n == 1:
    #     return n
    # return fibonacci(n-1) + fibonacci(n-2)
    
    ret = [0, 1]
    # [ret.append(ret[-1]+ret[-2]) for _ in range(2, n+1)] 
    for _ in range(2, n+1):
        ret.append(ret[-1]+ret[-2])
    return ret[n]

def sum(n: int) -> int: # O(n) | O(1)
    """
    Function that computes the sum of all integers from 0 to n.
    :param n: The number to compute the sum up to
    :return: The sum of all integers from 0 to n
    """
    # sum_ = 0
    # for i in range(n, 0, -1):
    #     sum_ += i
    # return sum_
    return (n*(n+1))/2

def square(n: int) -> int:
    """
    Function that computes the square of a number.
    :param n: The number to compute the square of
    :return: The square of n
    """
    return n**2



def is_prime(n: int) -> bool: # O(n) | O(sqrt(n))
    import math
    """
    Function that checks if a number is prime.
    A prime number is a number that is divisible only by itself and 1.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n == 0 or n == 1:
        return False

    for i in range(2, math.floor(n**(1/2))+1):
        if n % i == 0:
            return False
    return True