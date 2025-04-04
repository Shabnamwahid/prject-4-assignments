import random

# Class to represent the Minesweeper game
class Minesweeper:
    def __init__(self, size=5, num_mines=5):
        self.size = size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]  # Empty board
        self.revealed = [[' ' for _ in range(size)] for _ in range(size)]  # Revealed cells
        self.mines = set()  # Set to store mine positions
        self.game_over = False
        self._place_mines()

    def _place_mines(self):
        # Randomly place mines on the board
        while len(self.mines) < self.num_mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.mines.add((x, y))

        # Update the board with mine positions
        for x, y in self.mines:
            self.board[x][y] = '*'

    def _get_neighbors(self, x, y):
        # Get all neighboring cells (8 possible directions)
        neighbors = []
        for i in range(max(0, x - 1), min(self.size, x + 2)):
            for j in range(max(0, y - 1), min(self.size, y + 2)):
                if (i, j) != (x, y):
                    neighbors.append((i, j))
        return neighbors

    def _get_adjacent_mines(self, x, y):
        # Count how many mines are adjacent to the given cell
        count = 0
        for nx, ny in self._get_neighbors(x, y):
            if (nx, ny) in self.mines:
                count += 1
        return count

    def _reveal(self, x, y):
        # Reveal the cell at (x, y) and recursively reveal neighbors if necessary
        if self.revealed[x][y] != ' ':
            return

        adjacent_mines = self._get_adjacent_mines(x, y)
        self.revealed[x][y] = str(adjacent_mines) if adjacent_mines > 0 else '0'

        if adjacent_mines == 0:
            for nx, ny in self._get_neighbors(x, y):
                if self.revealed[nx][ny] == ' ':
                    self._reveal(nx, ny)

    def reveal_cell(self, x, y):
        if (x, y) in self.mines:
            self.game_over = True
            print(f"Game Over! You hit a mine at ({x}, {y}).")
        else:
            self._reveal(x, y)

    def display_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.revealed[i][j], end=' ')
            print()

# Function to play the game
def play_game():
    # Initialize the game
    game = Minesweeper(size=5, num_mines=5)

    while not game.game_over:
        game.display_board()
        try:
            x, y = map(int, input("Enter row and column (0-based index) to reveal (e.g. 1 2): ").split())
            if 0 <= x < game.size and 0 <= y < game.size:
                game.reveal_cell(x, y)
            else:
                print("Invalid input. Please enter valid row and column.")
        except ValueError:
            print("Invalid input. Please enter two integers.")

    game.display_board()
    print("Game Over!")

if __name__ == "__main__":
    play_game()
