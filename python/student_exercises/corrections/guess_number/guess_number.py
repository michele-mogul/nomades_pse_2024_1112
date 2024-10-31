import random
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    # for dychtomy optimal search, the formula is the following: log2(100)

    # Generate a random number between 1 and 100
    MAX_NUMBER = 100
    secret_number = random.randint(1, MAX_NUMBER)
    print(secret_number)
    optimal_attempt_count = math.ceil(math.log2(MAX_NUMBER))
    
    input_number = int(input("Guess the number \n"))
    attempt_count = 1
    while input_number != secret_number:
        if input_number < secret_number:
            print("too low")
        else:
            print("too high")
        
        input_number = int(input("Guess the number \n"))
        attempt_count += 1

    print(secret_number)
    congrats = "Bravo, " if attempt_count <= optimal_attempt_count else ""
    print(f"{congrats}optimal attempt number is {optimal_attempt_count} you did {attempt_count}")

if __name__ == '__main__':
    # Run the game
    guess_number()
