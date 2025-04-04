import time

# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the game is won
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

# Function to check if the board is full
def is_full(board):
    return " " not in board

# Function to play the game
def play_game():
    board = [" " for _ in range(9)]  # Initializing the board
    current_player = "X"  # X always starts
    game_over = False

    while not game_over:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        
        # Check if the move is valid
        if board[move] == " ":
            board[move] = current_player
        else:
            print("This spot is taken! Try again.")
            continue

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        # Check if the board is full
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"
        
        time.sleep(1)  # Add a short delay for better UX

# Start the game
if __name__ == "__main__":
    play_game()
