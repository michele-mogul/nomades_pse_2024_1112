import os
import random
import time
from random import randint


# Function to draw the tic-tac-toe board
def draw_board(board: list[str]) -> None:
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """

    board_str = f"""
    |1|2|3|       {board[0]} | {board[1]} | {board[2]}                         
    |4|5|6|       {board[3]} | {board[4]} | {board[5]}              
    |7|8|9|       {board[6]} | {board[7]} | {board[8]}                                                    
                   

    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(board_str)

def check_win(board: list[str], player: str) -> bool:
    #create a check board which is a list of 3 lists
    win_list = []
    # Rows
    for i in range(0, 9, 3):
        win_list.append(set(board[i:i + 3]))

    # Columns
    for i in range(3):
        win_list.append(set(board[i::3]))

    # Diagonals
    win_list.append(set(board[0::4]))
    win_list.append(set(board[2:8:2]))

    return any(all(x == player for x in win_combination) for win_combination in win_list)



# Function to play the game
def play_game():
    # The board variable store the state of the game, where board[0] is the top left corner and board[8] is the bottom right corner
    board = [' '] * 9

    current_player = random.choice(['X','O'])
    # the game_over variable is used to know if the game is running or not
    game_over  = False

    while not game_over:
        draw_board(board)
        move = input(f"Its player {current_player} move. Enter the number of the cell:")

        try:
            move = int(move)
            if 9 < move < 1 or board[move - 1] != ' ':
                raise ValueError

            board[move-1] = current_player
            draw_board(board)
            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                game_over = True
            elif ' ' not in board:
                print("Draw!")
                game_over = True
            else:
                current_player = ('X', 'O')[current_player == 'X']


        except ValueError:
            print("Invalid move. Try again!")
            time.sleep(0.7)
            continue

# Start the game
if __name__ == "__main__":
    play_game()
