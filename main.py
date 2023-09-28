field = [
    ['.' for _ in range(3)]  # массив из точек 3 на 3
    for _ in range(3)
]


def print_field():      #вывод поля
    for row in field:   #что значит этот блок
        for cell in row:
            print(cell, end=' ')
        print()


print_field()


def player_move():          #ход игрока
    print('Please enter your move (row,col): ') #пишет что надо написать свой ход
    move = input()
    row, col = move.split(',') #я так понял если нету разделителя он его поставит
    row, col = int(row) - 1, int(col) - 1 #зачем вычитаются 1 не знаю

    if field[row][col] != '.':  #проверяет что расположено на выбранном месте
        print('Cell is already taken')  #если там уже что то кроме . то пишет что занято
    else:
        field[row][col] = 'X'   #если нет то ставит X


# ход компьютера
from random import randint  #компьютер рандомно выбирает своей ход


def ai_move():
    x = randint(0, 2)
    y = randint(0, 2)
    while field[x][y] != '.':
        x = randint(0, 2)
        y = randint(0, 2)
    field[x][y] = 'O'

#массив с вариантами победы
WINS = [
    [(0, 0), (0, 1), (0, 2)],  # 0-я строка
    [(1, 0), (1, 1), (1, 2)],  # 1-я строка
    [(2, 0), (2, 1), (2, 2)],  # 2-я строка
    [(0, 0), (1, 0), (2, 0)],  # 0-й столбец
    [(0, 1), (1, 1), (2, 1)],  # 1-й столбец
    [(0, 2), (1, 2), (2, 2)],  # 2-й столбец
    [(0, 0), (1, 1), (2, 2)],  # главная диагональ
    [(0, 2), (1, 1), (2, 0)]  # побочная диагональ
]

#какая то хуета
def check_win():
    for option in WINS:
        # print(f'Checking option {option}:')
        values = []
        for cell in option:
            row, col = cell
            value = field[row][col]
            # print(f'\t-cell {cell} has value {value}')
            values.append(value)
        if values[0] == values[1] == values[2] != '.':
            # print(f'All values are equal to {values[0]}, returning!')
            return values[0]


check_win()
#вывод выйгрыша или пройгрыша
while True:
    player_move()
    print_field()
    if check_win() == 'X':
        print('You won!')
        break
    ai_move()
    print_field()
    if check_win() == 'O':
        print('Computer wins!')
        break
