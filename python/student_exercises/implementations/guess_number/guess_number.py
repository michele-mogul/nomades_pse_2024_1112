import random
import math


def get_non_negative_int(prompt):
    while True:
        try:
            _input_value = int(input(prompt))
        except ValueError:
            print("Sorry, you should enter an integer.")
            continue

        if _input_value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return _input_value


def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    # for dychtomy optimal search, the formula is the following: log2(100)

    # Generate a random number between 1 and 100
    secret_number: int  = random.randint(1, 100)
    optimal_tries: int  = int(math.log(100, 2))
    print(secret_number)
    trys: int  = 1
    while (input_data := get_non_negative_int("Try you luck! Enter a number\n")) != secret_number:
        trys += 1
        print(f"Try again!, your secret number is {'higher' if secret_number > input_data else 'lower'}")

    # to ask user to enter the number use the function input
    print(f"bravo, you did it in {trys} {('try', 'tries')[trys > 1]}!")
    print(f"the optimal ties are {optimal_tries} for this range, you did {('optimal!','good.')[trys > optimal_tries]}")

if __name__ == '__main__':
    # Run the game
    guess_number()


