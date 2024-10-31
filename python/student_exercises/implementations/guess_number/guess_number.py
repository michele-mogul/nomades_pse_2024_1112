import random
import math


# Question: The definition position of the function determines the visibility in the global namespace? This also applies
# for classes or not?
def get_non_negative_int_input(prompt):
    input_value_casted = -1
    while True:
        try:
            input_value = input(prompt)
            if input_value == 'exit':
                return -1
            input_value_casted = int(input_value)
        except ValueError:
            print("Sorry, you should enter an integer.")
            continue

        if input_value_casted < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return input_value_casted


def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    # for dychtomy optimal search, the formula is the following: log2(100)

    # Generate a random number between 1 and 100
    print("Welcome to the guess number game! Try your luck!")
    print("Enter a number and see if you guessed right!")
    print("If you want to exit, enter the word 'exit'")

    MAX_NUMBER = 100
    tries_count, secret_number, optimal_tries_count  = 1, random.randint(1, MAX_NUMBER), int(math.log(MAX_NUMBER, 2))

    print(secret_number)
    while (input_data := get_non_negative_int_input("Try you luck! Enter a number\n")) != secret_number and input_data != -1:
        print(f"Try again!, your secret number is {'higher' if secret_number > input_data else 'lower'}")
        tries_count += 1
    else:
        if input_data == -1:
            print("Okey Dokey! See you next time!")
            return
        # to ask user to enter the number use the function input
        print(f"bravo, you did it in {tries_count} {('try', 'tries')[tries_count > 1]}!")
        print(f"the optimal ties are {optimal_tries_count} for this range, you did {('great!','good.')[tries_count > optimal_tries_count]}")

if __name__ == '__main__':
    # Run the game
    guess_number()


