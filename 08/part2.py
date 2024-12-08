from itertools import combinations


def solution(file_name: str) -> int:
    """
    main driver function
    """
    box = []
    antennas_map = {}
    anti_nodes = set()

    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            chars = list(line)
            box.append(chars)

    find_antennas(antennas_map, box)
    for key, value in antennas_map.items():
        unique_pairs = generate_unique_pairs(value)
        for unique_pair in unique_pairs:
            process_unique_pair(unique_pair, box, anti_nodes)

    return len(anti_nodes)


def process_unique_pair(unique_pair: tuple[int, int, int, int], box: list[list[str]], anti_nodes: set[tuple[int, int]]):
    X = len(box)
    Y = len(box[0])
    first_antenna = (unique_pair[0], unique_pair[1])
    second_antenna = (unique_pair[2], unique_pair[3])
    distance = (first_antenna[0] - second_antenna[0], first_antenna[1] - second_antenna[1])
    first_anti_node = first_antenna
    while 0 <= first_anti_node[0] < X and 0 <= first_anti_node[1] < Y:
        anti_nodes.add(first_anti_node)
        first_anti_node = (first_anti_node[0] + distance[0], first_anti_node[1] + distance[1])

    second_anti_node = second_antenna
    while 0 <= second_anti_node[0] < X and 0 <= second_anti_node[1] < Y:
        anti_nodes.add(second_anti_node)
        second_anti_node = (second_anti_node[0] - distance[0], second_anti_node[1] - distance[1])


def find_antennas(antennas_map: dict[str, list[tuple[int, int]]], box: list[list[str]]):
    for i in range(len(box)):
        for j in range(len(box[0])):
            curr = box[i][j]
            if curr != ".":
                if curr in antennas_map:
                    antennas_map[curr].append((i, j))
                else:
                    antennas_map[curr] = [(i, j)]


def generate_unique_pairs(tuples_list):
    """
    Generates all unique pairs of tuples from the given list of tuples.

    :param tuples_list: A list of tuples, where each tuple contains 2 integers.
    :return: A list of tuples, where each tuple contains 4 integers.
    """
    unique_pairs = []

    # Generate all combinations of pairs from the list of tuples
    for (a1, b1), (a2, b2) in combinations(tuples_list, 2):
        unique_pairs.append((a1, b1, a2, b2))

    return unique_pairs


print(solution("./input.txt"))
