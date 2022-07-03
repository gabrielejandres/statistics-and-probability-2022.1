import numpy
import sys

INFINITY = 1000000


def create_positions_matrix():
    return numpy.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])


def update_position(board, path, position):
    board[position] += 1
    path.append(position)
    return board, path


def print_board(board):
    print("__________")
    for i in board:
        print("|", end="")
        print("\t".join(map(str, i)), end="")
        print("|")
    print("__________\n")


def get_adjacents(position):
    adjacents = []

    row = position[0]
    column = position[1]

    if row + 1 != 3:
        adjacents.append((row + 1, column))

    if row - 1 != -1:
        adjacents.append((row - 1, column))

    if column + 1 != 3:
        adjacents.append((row, column + 1))

    if column - 1 != -1:
        adjacents.append((row, column - 1))

    return adjacents


def get_next_position(position):
    adjacents = get_adjacents(position)
    num_adjacents = len(adjacents)
    adjacents_indexes = [i for i in range(num_adjacents)]
    probabilities = [1/num_adjacents] * num_adjacents #array de probabilidades com base no numero de adjacentes
    index_next_position = numpy.random.choice(adjacents_indexes, p=probabilities)

    return adjacents[index_next_position]


def walk_in_board(board, path, position):
    board, path = update_position(board, path, position)
    if position != (0, 0) and position != (2, 2):
        board, trap = walk_in_board(board, path, get_next_position(position))
    elif position == (0, 0):
        trap = (0, 0)
    elif position == (2, 2):
        trap = (2, 2)

    return board, trap


def print_path(path):
    print("Caminho percorrido pelo inseto: ", end="")
    for position in path:
        print(position, end="")
        if path.index(position) != (len(path) - 1):
            print(" -> ", end="")


def get_initial_position():
    row = int(input('Digite a linha da posicao inicial (0-2): '))
    column = int(input('Digite a coluna da posicao inicial (0-2): '))

    if row not in range(0, 3) or column not in range(0, 3):
        print("Posicao invalida. As posicoes devem ir de 0 a 2 somente, tanto nas linhas quanto nas colunas.")
        sys.exit()

    return row, column


def simulate_bug_movement():
    board = create_positions_matrix()
    path = []

    print("=== Tabuleiro 3x3 inicial ===")
    print_board(board)

    initial_position = get_initial_position()

    print("\n=== Tabuleiro 3x3 final ===")
    final_board, trap = walk_in_board(board, path, initial_position)
    print_board(final_board)

    print_path(path)
    print("\nArmadilha:", trap)


def approach_probabilities_of_trap_catches(limit, all, position = (0, 0)):
    if all:
        for i in range(0, 3):
            for j in range(0, 3):
                initial_position = (i, j)

                first_trap_catches = 0
                second_trap_catches = 0

                for _ in range(limit):
                    board = create_positions_matrix()
                    path = []
                    board, trap = walk_in_board(board, path, initial_position)
                    if trap == (0, 0):
                        first_trap_catches += 1
                    elif trap == (2, 2):
                        second_trap_catches += 1

                print(f'== Posicao inicial {initial_position} ==')
                print(f'Probabilidade do inseto ser capturado pela primeira armadilha (0,0): {first_trap_catches/limit * 100}%')
                print(f'Probabilidade do inseto ser capturado pela segunda armadilha (2,2): {second_trap_catches/limit * 100}%\n')
    else:
        first_trap_catches = 0
        second_trap_catches = 0

        for _ in range(limit):
            board = create_positions_matrix()
            path = []
            board, trap = walk_in_board(board, path, position)
            if trap == (0, 0):
                first_trap_catches += 1
            elif trap == (2, 2):
                second_trap_catches += 1

        print(f'== Posicao inicial {position} ==')
        print(f'Probabilidade do inseto ser capturado pela primeira armadilha (0,0): {first_trap_catches / limit * 100}%')
        print(f'Probabilidade do inseto ser capturado pela segunda armadilha (2,2): {second_trap_catches / limit * 100}%\n')


def approach_average_hops_number(limit, all, position = (0, 0)):
    if all:
        for i in range(0, 3):
            for j in range(0, 3):
                initial_position = (i, j)
                hops_average = 0

                for _ in range(limit):
                    board = create_positions_matrix()
                    path = []
                    board, trap = walk_in_board(board, path, initial_position)

                    hops = board.sum() - 1  # subtraio 1 por causa do "salto" para a posição inicial que eh considerado
                    hops_average += hops

                hops_average /= limit
                print(f'== Posicao inicial {initial_position} ==')
                print(f'Numero medio de saltos eh: {hops_average}\n')
    else:
        hops_average = 0

        for _ in range(limit):
            board = create_positions_matrix()
            path = []
            board, trap = walk_in_board(board, path, position)

            hops = board.sum() - 1  # subtraio 1 por causa do "salto" para a posição inicial que eh considerado
            hops_average += hops

        hops_average /= limit
        print(f'== Posicao inicial {position} ==')
        print(f'Numero medio de saltos eh: {hops_average}\n')


def approach_average_central_position_visits(limit, initial_position):
    visits_average = 0

    for _ in range(limit):
        board = create_positions_matrix()
        path = []
        board, trap = walk_in_board(board, path, initial_position)

        visits_average += board[1][1]

    visits_average /= limit
    print(f'== Posicao inicial {initial_position} ==')
    print(f'Numero medio de visitas a casa central eh: {visits_average}\n')


if __name__ == '__main__':
    # b
    print("Simulacao de um movimento completo do inseto no tabuleiro")
    simulate_bug_movement()

    # c
    print("\nProbabilidades de ser capturado por cada uma das armadilhas por posicao inicial")
    approach_probabilities_of_trap_catches(10000, True)
    # approach_probabilities_of_trap_catches(10000, False, get_initial_position())

    # d
    print("\nNumero medio de saltos por posicao inicial")
    approach_average_hops_number(10000, True)
    # approach_average_hops_number(10000, False, get_initial_position())

    # e
    print("\nNumero medio de visitas a casa central")
    approach_average_central_position_visits(10000, (2, 0))
