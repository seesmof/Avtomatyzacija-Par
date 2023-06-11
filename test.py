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
        # Get all neighbors of a cell
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Skip the current cell
                if i == 0 and j == 0:
                    continue
                # Skip cells that are out of the board
                elif row + i < 0 or row + i >= self.size or col + j < 0 or col + j >= self.size:
                    continue
                else:
                    neighbors.append(self.board[row+i][col+j].state)
        return neighbors

    def apply_rules(self):
        # Create a new board to store the next generation
        new_board = [[Cell(0) for _ in range(self.size)]
                     for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                state = self.board[i][j].state
                neighbors = self.get_neighbors(i, j)
                live_neighbors = sum(neighbors)
                # If a cell is alive and has fewer than 2 neighbors, it dies
                if state == 1 and live_neighbors < 2:
                    new_board[i][j].state = 0
                # If a cell is alive and has 2 or 3 neighbors, it lives
                elif state == 1 and (live_neighbors == 2 or live_neighbors == 3):
                    new_board[i][j].state = 1
                # If a cell is alive and has more than 3 neighbors, it dies
                elif state == 1 and live_neighbors > 3:
                    new_board[i][j].state = 0
                # If a cell is dead and has exactly 3 neighbors, it comes to life
                elif state == 0 and live_neighbors == 3:
                    new_board[i][j].state = 1
        # Update the board with the new generation
        self.board = new_board

    def display(self):
        # Print the board
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].state == 1:
                    print("🔴 ", end="")
                else:
                    print("  ", end="")
            print()
        print()


def get_menu_choice():
    # Get user input for board size, mode, and speed
    print("\n\033[1mЛаскаво просимо!\033[0m\n")
    board_size = input("Введіть розмір дошки: ")
    mode = input(
        "\nЯк би ви хотіли грати?\n1. Спостерігайте за грою\n2. Підтверджувати кожен крок\n: ")
    speed = "2"
    if mode == "1":
        speed = input(
            "\nОберіть швидкіст гри\n1. Повільна\n2. Середня\n3. Швидка\n4. Найшвидша\n: ")
    return board_size + "," + mode + "," + speed


def main():
    # Run the Game of Life simulation
    choice = get_menu_choice()
    print()
    board_size, mode, speed = choice.split(",")

    # Convert speed input to a float
    if speed == "1":
        speed = 2
    elif speed == "2":
        speed = 1
    elif speed == "3":
        speed = 0.5
    else:
        speed = 0.15

    # Create the board and start the simulation
    board = Board(int(board_size))
    counter = 0
    while True:
        board.apply_rules()
        print("\n\033[90mПокоління " + str(counter) + "\033[0m\n")
        board.display()
        print("\n")
        counter += 1

        # Wait for user input or a certain amount of time
        if mode == "1":
            time.sleep(speed)
        else:
            input("\033[37mPress enter to continue...\033[0m\n")

        # If all cells are dead, end the simulation
        if all(cell.state == 0 for row in board.board for cell in row):
            print(
                f"\033[1mВітаємо!\033[0m\nГра завершилась після {counter} {'поколінь' if counter == 1 else 'покоління'}.\n")
            break


if __name__ == "__main__":
    main()
