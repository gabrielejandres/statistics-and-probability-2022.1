import numpy

N = 5000
INFINITY = 1000000


def update_number_of_visits(vertex, num_visits_by_vertex):
    num_visits_by_vertex[vertex] = num_visits_by_vertex[vertex] + 1
    return num_visits_by_vertex


def get_next_position(actual_vertex):
    previous_vertex = 11 if actual_vertex == 0 else actual_vertex - 1
    next_vertex = 0 if actual_vertex == 11 else actual_vertex + 1
    return numpy.random.choice([previous_vertex, next_vertex], p=[1/2, 1/2])


def check_all_visited(num_visits_by_vertex):
    return 0 not in num_visits_by_vertex.values()


def get_y(num_visits_by_vertex):
    return sum(num_visits_by_vertex.values())


def simulate_y():
    num_visits_by_vertex = dict(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    all_visited = False
    actual_vertex = 0
    num_visits_by_vertex = update_number_of_visits(actual_vertex, num_visits_by_vertex)

    while not all_visited:
        next_v = get_next_position(actual_vertex)
        # print(f'Próximo vértice a ser visitado: {next_v}')
        num_visits_by_vertex = update_number_of_visits(next_v, num_visits_by_vertex)
        actual_vertex = next_v
        all_visited = check_all_visited(num_visits_by_vertex)

    y = get_y(num_visits_by_vertex)
    return y


def approach_expected_value_of_y(N):
    return (1/N) * sum(simulate_y() for _ in range(1, N + 1))


def get_probability_mass_function(limit):
    num_visits_by_vertex = dict(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    actual_vertex = 0
    num_visits_by_vertex = update_number_of_visits(actual_vertex, num_visits_by_vertex)

    for _ in range(limit):
        next_v = get_next_position(actual_vertex)
        num_visits_by_vertex = update_number_of_visits(next_v, num_visits_by_vertex)
        actual_vertex = next_v

    prob_mass_function = []

    for vertex in range(0, 12):
        prob_mass_function.append(num_visits_by_vertex.get(vertex) / limit)

    return prob_mass_function


if __name__ == '__main__':
    # a
    y = simulate_y()
    print(f'Simulacao do numero de passos (variavel aleatoria Y) eh: {y}')

    # b
    expected_value = approach_expected_value_of_y(N)
    print(f'O valor aproximado para E[Y] eh: {expected_value}')

    # c
    probability_mass_function = get_probability_mass_function(INFINITY)
    print(f'Valores da f.m.p apos {INFINITY}s:')
    for i in range(0, 12):
        print(f'P(Z = {i}) = {probability_mass_function[i]} -> Probabilidade de {probability_mass_function[i] * 100}% de estar no vertice {i}')