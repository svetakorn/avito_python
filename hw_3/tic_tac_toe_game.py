from typing import List
from colors import blue, yellow
import re


def char_to_num(char: str) -> int:
    """Переводит заголовки строк (a,b,c) в числа для дальнейших операций с матрицей"""
    return ord(char) - 97


def num_to_char(num: int) -> str:
    """Переводит числа в заголовки строк для вывода доски"""
    return str(chr(97 + num))


def get_board_size() -> int:
    """Получает от пользователя размер доски и обрабатывает ввод"""
    print('Привет! Это крестики-нолики, давайте играть :) \n')
    while True:
        input_value = input('-- Введите размер квадратного поля (целое число от 3 до 5): \n')
        try:
            board_size = int(input_value)
            if board_size in range(3, 6):
                return board_size
            else:
                print('Введенное число должно быть от 3 до 5 включительно')
        except ValueError:
            print('Это не целое число, попробуйте еще раз')


def color_mark(mark: str) -> str:
    """Разукрашивает метки для вывода на доску"""
    if mark == 'x':
        return blue(mark)
    elif mark == 'o':
        return yellow(mark)
    else:
        return ' '


def show_board(board_matrix: List):
    """Выводит в консоль доску с игрой"""
    size = len(board_matrix)
    print('\n  | ' + ' | '.join([str(x + 1) for x in range(size)]) + ' |')
    print('-' * (3 + 4 * size))
    for i, row in enumerate(board_matrix):
        print(f'{num_to_char(i)} | '
              + ' | '.join([color_mark(x) for x in row]) + ' |')
        print('-' * (3 + 4 * size))


def get_player_mark(player_id: int) -> str:
    """Получает по id игрока метку, которую игрок использует в игре"""
    switcher = {
        1: 'x',
        2: 'o'
    }
    return switcher.get(player_id, 'Несуществуюший игрок')


def make_move(board_matrix: List, player_id: int):
    """Предлагает игроку сделать ввод хода в консоли и обрабатывает полученное значение"""
    while True:
        input_move = str(input(f'-- Ваш ход (игрок {player_id}): \n'))
        try:
            move = re.search(r'^([a-z])(\d+)$', input_move)
            row = char_to_num(move.group(1))
            column = int(move.group(2)) - 1

            if row < 0 or column < 0:
                raise Exception

            if board_matrix[row][column] is None:
                board_matrix[row][column] = get_player_mark(player_id)
                break
            else:
                print('Клетка уже занята, попробуйте снова')
        except Exception:
            print('Неверный ввод хода, попробуйте еще раз')


def check_win_rows(board_matrix: List) -> bool:
    """
    Проверяет, заполнил ли хотя бы один игрок хотя бы одну строку своими метками полностью.
    Если да, то этот игрок и будет победителем.
    """
    for row in board_matrix:
        if len(set(row)) == 1:
            if row[0] is not None:
                return True


def check_win_columns(board_matrix: List) -> bool:
    """
    Проверяет, заполнил ли хотя бы один игрок хотя бы один столбец своими метками полностью.
    Если да, то этот игрок и будет победителем.
    """
    transposed_matrix = list(map(list, zip(*board_matrix)))
    return check_win_rows(transposed_matrix)


def check_win_diag(board_matrix: List) -> bool:
    """
    Проверяет, заполнил ли хотя бы один игрок хотя бы одну диагональ своими метками полностью.
    Если да, то этот игрок и будет победителем.
    """
    if len(set([board_matrix[i][i] for i in range(len(board_matrix))])) == 1:
        if board_matrix[0][0] is not None:
            return True
    if len(set([board_matrix[i][len(board_matrix) - i - 1]
                for i in range(len(board_matrix))])) == 1:
        if board_matrix[0][len(board_matrix) - 1] is not None:
            return True


def check_draw(move_count: int, board_size: int) -> bool:
    """Проверяет, заполнены ли все клетки на доске. Если да, то это ничья"""
    if move_count == board_size ** 2:
        return True


def game():
    """Содержит логику игры крестики-нолики"""
    board_size = get_board_size()
    matrix = [[None] * board_size for _ in range(board_size)]
    show_board(matrix)

    move_count = 0
    while True:
        player_id = (move_count % 2) + 1
        make_move(matrix, player_id)
        show_board(matrix)

        if check_win_rows(matrix) or check_win_columns(matrix) or check_win_diag(matrix):
            print(f'Игрок {player_id} победил 🎉')
            break
        elif check_draw(move_count, board_size):
            print('Поле полностью заполнено - это ничья')
            break

        move_count += 1


if __name__ == '__main__':
    game()
