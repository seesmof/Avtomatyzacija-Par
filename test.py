import random
import time


class Cell:
    def __init__(self, state):
        self.state = state


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[Cell(random.randint(0, 1))
                       for _ in range(size)] for _ in range(size)]

    def get_neighbors(self, row, col):
        # Returns a list of the states of the 8 neighbors of the cell at (row, col)
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif row + i < 0 or row + i >= self.size or col + j < 0 or col + j >= self.size:
                    continue
                else:
                    neighbors.append(self.board[row+i][col+j].state)
        return neighbors

    def apply_rules(self):
        # Applies the rules of the game to each cell and updates its state
        new_board = [[Cell(0) for _ in range(self.size)]
                     for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                state = self.board[i][j].state
                neighbors = self.get_neighbors(i, j)
                live_neighbors = sum(neighbors)
                if state == 1 and live_neighbors < 2:
                    new_board[i][j].state = 0
                elif state == 1 and (live_neighbors == 2 or live_neighbors == 3):
                    new_board[i][j].state = 1
                elif state == 1 and live_neighbors > 3:
                    new_board[i][j].state = 0
                elif state == 0 and live_neighbors == 3:
                    new_board[i][j].state = 1
        self.board = new_board

    def display(self):
        # Displays the board
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].state == 1:
                    print("🔴 ", end="")
                else:
                    print("  ", end="")
            print()
        print()


def get_menu_choice():
    print("\nWelcome to the Game of Life!")
    board_size = input("\nEnter board size: ")
    mode = input(
        "\nHow would you like to play?\n1. Watch game play itself\n2. Confirm each move\n: ")
    return board_size + "," + mode


# Example usage
choice = get_menu_choice()
print()
board_size, mode = choice.split(",")
board = Board(int(board_size))
board.display()
while True:
    board.apply_rules()
    print("\n")
    board.display()
    print("\n")
    if mode == "1":
        time.sleep(1)
    else:
        input("Press enter to continue...\n")
