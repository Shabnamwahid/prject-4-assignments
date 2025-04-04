import math
import random

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check for winner
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check if the board is full
def is_full(board):
    return " " not in board

# Minimax Algorithm to calculate the best move for AI
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):  # If AI wins
        return 1
    elif check_win(board, "O"):  # If Human wins
        return -1
    elif is_full(board):  # If tie
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(board, depth + 1, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(board, depth + 1, True))
                board[i] = " "
        return best

# AI's best move
def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            move_val = minimax(board, 0, False)
            board[i] = " "
            if move_val > best_val:
                move = i
                best_val = move_val
    return move

# Function to play the game
def play_game():
    board = [" " for _ in range(9)]
    current_player = "O"  # Human starts
    game_over = False

    while not game_over:
        print_board(board)

        if current_player == "O":  # Human's turn
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif is_full(board):
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = "X"
            else:
                print("Invalid move, try again.")
        else:  # AI's turn
            move = best_move(board)
            board[move] = current_player
            print(f"AI chooses {move + 1}")
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O"

# Start the game
if __name__ == "__main__":
    play_game()
