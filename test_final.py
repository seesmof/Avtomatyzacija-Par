from colorama import Fore, Back, Style

cycle = 0


def print_pole(pole, count):
    if count == 0:
        print("\n  ╔═ Початкове поле:")
    else:
        print(f"  ╔═ Крок {count}:")
    for row in pole:
        print("  ║ ", end="")
        for cell in row:
            if cell == 1:
                print(Fore.GREEN+"▩"+Fore.RESET, end=" ")
            else:
                print(Fore.RED + "▩" + Fore.RESET, end=" ")
        print()
    print("  ╚═", end="")


def get_neighbours(pole, row, col):
    rows = len(pole)
    cols = len(pole[0])
    count = 0

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1),
               (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]
        if 0 <= offset_row < rows and 0 <= offset_col < cols and pole[offset_row][offset_col] == 1:
            count += 1
    return count


def update_pole(pole):
    global cycle
    new_pole = []
    for row in range(len(pole)):
        new_row = []
        for col in range(len(pole[row])):
            cell = pole[row][col]

            live_neighbours = get_neighbours(pole, row, col)

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
    count = 0

    print(" " * 23 + Fore.LIGHTYELLOW_EX + "\033[1m｡☆✼★━━━━━━━━━━━━►▬ Вітаємо! ▬◄━━━━━━━━━━━━★✼☆｡\n" + Fore.RESET + Fore.RED +
          " " * 32 + "▓▓" + Fore.RESET + " Це гра про життя клітин " + Fore.GREEN + "▓▓" + Fore.CYAN + """
    ╔──────────────────────────────────── ¤ Правила ¤ ───────────────────────────────────╗
    ║ 1. Клітина вмирає якщо вона має менше двох, або більше трьох живих клітин сусідів; ║
    ║ 2. Жива клітина, яка має дві або три живі клітин сусідів, продовжує жити;          ║
    ║ 3. Мертва клітина, у якій рівно три живі клітини серед сусідів, стає живою.        ║
    ╚═─────────────────────────────────── ¤¤¤¤¤¤¤¤¤¤¤ ──────────────────────────────────═╝
    \033[0m""" + Fore.RESET)

    size = int(input("  =───────> Введіть розмір поля: "))
    print(
        f"  => Введіть початкову конфігурацію поля {size}x{size} (1 - жива клітина, 0 - мертва клітина):")

    pole = []

    for i in range(size):
        print("  -> ", end="")
        ryad = list(map(int, input().split()))
        pole.append(ryad)

    print_pole(pole, count)
    print(' Для наступного кроку натисніть Enter. Для виходу введіть "0"')

    boards = []

    while input() != "0":
        count += 1
        boards.append(pole)
        pole = update_pole(pole)

        print_pole(pole, count)

        if all(cell == 0 for row in pole for cell in row):
            print(" Гру завершено! На полі немає живих клітин.")
            break
        elif pole in boards:
            print(" Гру завершено! На полі немає змін.")
            break

    print(Fore.CYAN+f"\n  Завершених життєвих циклів: " +
          Fore.GREEN+f"{cycle}"+Fore.RESET)


start_game()
