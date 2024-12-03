def solution(file_name: str) -> int:
    """
    main driver function
    """
    result = 0
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            line_length = len(line)
            for i in range(line_length):
                val = process_multiply(line, i, line_length)
                if val > 0:
                    result += val
    return result


def process_multiply(line: str, curr_index: int, line_length: int) -> int:
    """
    attempts to process and find the suitable substring for multiplication
    """
    if not is_char_present(line, curr_index, line_length, "m"):
        return 0
    curr_index += 1

    if not is_char_present(line, curr_index, line_length, "u"):
        return 0
    curr_index += 1

    if not is_char_present(line, curr_index, line_length, "l"):
        return 0
    curr_index += 1

    if not is_char_present(line, curr_index, line_length, "("):
        return 0
    curr_index += 1

    first_num = 0
    while curr_index < line_length and line[curr_index].isdigit():
        first_num = first_num * 10 + int(line[curr_index])
        curr_index += 1
    if first_num == 0:
        return 0

    if not is_char_present(line, curr_index, line_length, ","):
        return 0
    curr_index += 1

    second_num = 0
    while curr_index < line_length and line[curr_index].isdigit():
        second_num = second_num * 10 + int(line[curr_index])
        curr_index += 1
    if second_num == 0:
        return 0

    if not is_char_present(line, curr_index, line_length, ")"):
        return 0

    return first_num * second_num


def is_char_present(line: str, curr_index: int, line_length: int, char: str) -> bool:
    """
    checks if a character is present
    """
    if curr_index >= line_length:
        return False
    if line[curr_index] != char:
        return False
    return True


print(solution("./input.txt"))
