from typing import Tuple


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

    X = len(box)
    Y = len(box[0])
    found_start = False
    start_i, start_j = 0, 0

    for i in range(X):
        for j in range(Y):
            if box[i][j] == "^":
                box[i][j] = "."
                found_start = True
                start_i, start_j = i, j
                break
        if found_start:
            break

    direction = (-1, 0)
    while start_i >= 0 and start_i < X and start_j >= 0 and start_j < Y:
        curr = box[start_i][start_j]
        if curr == ".":
            box[start_i][start_j] = "X"
            result += 1
        elif curr == "#":
            start_i -= direction[0]
            start_j -= direction[1]
            direction = change_direction(direction)
        start_i += direction[0]
        start_j += direction[1]

    return result


def change_direction(initial_direction: Tuple[int]) -> Tuple[int]:
    if initial_direction == (-1, 0):
        return (0, 1)
    elif initial_direction == (0, 1):
        return (1, 0)
    elif initial_direction == (1, 0):
        return (0, -1)
    elif initial_direction == (0, -1):
        return (-1, 0)
    else:
        return initial_direction


print(solution("./input.txt"))
