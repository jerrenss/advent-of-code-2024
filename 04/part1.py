from typing import List


def solution(file_name: str) -> int:
    """
    main driver function
    """
    box = []
    result = 0
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if len(stripped) > 0:
                box.append(list(stripped))

    X = len(box)
    Y = len(box[0])

    for i in range(X):
        for j in range(Y):
            result += searchStart(box, X, Y, i, j, 0)

    return result


def searchStart(box: List[List[str]], X: int, Y: int, i: int, j: int, index: int) -> int:
    if box[i][j] != "X":
        return 0
    return searchRest(box, X, Y, i, j, 1, -1, -1) + \
        searchRest(box, X, Y, i, j, 1, 0, -1) + \
        searchRest(box, X, Y, i, j, 1, +1, -1) + \
        searchRest(box, X, Y, i, j, 1, -1, 0) + \
        searchRest(box, X, Y, i, j, 1, +1, 0) + \
        searchRest(box, X, Y, i, j, 1, -1, +1) + \
        searchRest(box, X, Y, i, j, 1, 0, +1) + \
        searchRest(box, X, Y, i, j, 1, +1, +1)


def searchRest(box: List[List[str]], X: int, Y: int, i: int, j: int, index: int, X_dir: int, Y_dir: int) -> int:
    new_i = i + X_dir
    new_j = j + Y_dir
    if new_i < 0 or new_i >= X or new_j < 0 or new_j >= Y:
        return 0
    curr = box[new_i][new_j]
    if index == 1:
        if curr != "M":
            return 0
    elif index == 2:
        if curr != "A":
            return 0
    elif index == 3:
        if curr != "S":
            return 0
        else:
            return 1
    return searchRest(box, X, Y, new_i, new_j, index + 1, X_dir, Y_dir)


print(solution("./input.txt"))
