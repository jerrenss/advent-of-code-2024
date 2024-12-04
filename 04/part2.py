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
    if box[i][j] != "A":
        return 0

    left_diag = (is_char_present(box, X, Y, i - 1, j - 1, "M") and is_char_present(box, X, Y, i + 1, j + 1, "S")
                 ) or (is_char_present(box, X, Y, i - 1, j - 1, "S") and is_char_present(box, X, Y, i + 1, j + 1, "M"))
    right_diag = (is_char_present(box, X, Y, i - 1, j + 1, "M") and is_char_present(box, X, Y, i + 1, j - 1, "S")
                  ) or (is_char_present(box, X, Y, i - 1, j + 1, "S") and is_char_present(box, X, Y, i + 1, j - 1, "M"))

    if left_diag and right_diag:
        return 1

    return 0


def is_char_present(box: List[List[str]], X: int, Y: int, i: int, j: int, char: str) -> bool:
    if i < 0 or i >= X or j < 0 or j >= Y:
        return False
    return box[i][j] == char


print(solution("./input.txt"))
