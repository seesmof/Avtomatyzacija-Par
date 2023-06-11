import time
from colorama import Fore, Back, Style
import os
cycle = 0


def print_pole(pole):
    for row in pole:
        print("║ ", end="")
        for cell in row:
            if cell == 1:
                print(Fore.GREEN+"▩"+Fore.RESET, end=" ")
            else:
                print(Fore.RED + "▩" + Fore.RESET, end=" ")
        print()


def get_neighbours(pole, row, col):
    rows = len(pole)
    cols = len(pole[0])
    count = 0
    # зсуви
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1),
               (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]
        if 0 <= offset_row < rows and 0 <= offset_col < cols and pole[offset_row][offset_col] == 1:
            count += 1
    return count

#   1 0 1 0
#   1 1 0 1
#   1 0 1 0
#   0 1 0 1


def update_pole(pole):
    global cycle
    new_pole = []
    for row in range(len(pole)):
        new_row = []
        for col in range(len(pole[row])):
            cell = pole[row][col]

            live_neighbours = get_neighbours(pole, row, col)
            # print(f"Клітина {row} - {col} має {live_neighbours} сусідів")
            if cell == 1:
                if live_neighbours in [2, 3]:
                    new_row.append(1)
                else:
                    cycle += 1
                    new_row.append(0)
            else:
                if live_neighbours == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)

        new_pole.append(new_row)
    return new_pole


def start_game():
    global cycle
    size = int(input("Введіть розмір поля: "))
    os.system('cls||clear')
    print(
        f"Введіть початкову конфігурацію поля {size}x{size} (1 - жива клітина, 0 - мертва клітина):")
    pole = []
    for i in range(size):
        print("-> ", end="")
        ryad = list(map(int, input().split()))
        pole.append(ryad)
    os.system('cls||clear')
    print("╔═ Початкове поле:")
    print_pole(pole)
    print("╚═", end="")
    print(' Для наступного кроку введіть будь-що. Для виходу введіть "0"')
    count = 0
    while input() != "0":
        count += 1
        old = pole
        pole = update_pole(pole)
        print(f"╔═ Крок {count}:")
        print_pole(pole)
        print("╚═", end="")

        # 1 0 1 0
        # 0 1 0 1
        # 0 0 1 1
        # 1 1 0 0

        if all(cell == 0 for row in pole for cell in row):
            print(" Гру завершено! На полі немає живих клітин.")
            break
        elif old == pole:
            print(" Гру завершено! На полі немає змін.")
            break
    print(f"Життєвих циклів: {cycle}")


start_game()
