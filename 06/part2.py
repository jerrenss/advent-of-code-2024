from typing import List, Tuple, Set


def solution(file_name: str) -> int:
    """
    main driver function
    """
    box = []
    result = 0

    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            char_list = list(line)
            box.append(char_list)

    path_set = set()
    start_i, start_j = find_start(box)
    initial_direction = (-1, 0)

    populate_path_set(box, initial_direction, path_set, start_i, start_j)

    for path in path_set:
        curr_i, curr_j = path
        if box[curr_i][curr_j] == "^":
            continue

        prev = box[curr_i][curr_j]
        box[curr_i][curr_j] = "#"

        if run_simulation(box, initial_direction, start_i, start_j):
            result += 1

        box[curr_i][curr_j] = prev

    return result


def find_start(box: List[List[str]]) -> Tuple[int]:
    X = len(box)
    Y = len(box[0])

    for i in range(X):
        for j in range(Y):
            if box[i][j] == "^":
                return (i, j)

    return (0, 0)


def populate_path_set(box: List[List[str]], direction: Tuple[int], path_set: Set[Tuple], start_i: int, start_j: int):
    X = len(box)
    Y = len(box[0])

    while start_i >= 0 and start_i < X and start_j >= 0 and start_j < Y:
        curr = box[start_i][start_j]
        if curr == "." or curr == "^":
            path_set.add((start_i, start_j))
        elif curr == "#":
            start_i -= direction[0]
            start_j -= direction[1]
            direction = change_direction(direction)
        start_i += direction[0]
        start_j += direction[1]


def run_simulation(box: List[List[str]], direction: Tuple[int], start_i: int, start_j: int) -> bool:
    X = len(box)
    Y = len(box[0])
    path_set = set()

    while start_i >= 0 and start_i < X and start_j >= 0 and start_j < Y:
        curr = box[start_i][start_j]
        if curr == "." or curr == "^":
            key = (start_i, start_j, direction)
            if key in path_set:
                return True
            path_set.add(key)
        elif curr == "#":
            start_i -= direction[0]
            start_j -= direction[1]
            direction = change_direction(direction)
        start_i += direction[0]
        start_j += direction[1]

    return False


def change_direction(direction: Tuple[int]) -> Tuple[int]:
    if direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    elif direction == (0, -1):
        return (-1, 0)
    else:
        return direction


print(solution("./input.txt"))
