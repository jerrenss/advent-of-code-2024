from itertools import product


def solution(file_name: str) -> int:
    """
    driver function
    """
    result = 0

    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            parts = line.split(":")
            if len(parts) != 2:
                continue
            nums_str = parts[1].strip().split()
            nums = list(map(int, nums_str))
            total = int(parts[0].strip())
            N = len(nums)
            all_operations = generate_all_operations(N - 1)
            for operations in all_operations:
                if perform_operation(total, nums, operations):
                    result += total
                    break

    return result


def generate_all_operations(length: int) -> list[tuple[str, ...]]:
    return list(product(["+", "*"], repeat=length))


def perform_operation(total: int, nums: list, operations: tuple[str, ...]) -> bool:
    curr_total = 0
    N = len(nums)
    for i in range(N):
        if i == 0:
            curr_total = nums[i]
            continue

        curr_num = nums[i]
        curr_operation = operations[i - 1]  # length of operations should be one less then nums

        if curr_operation == "+":
            curr_total += curr_num
        elif curr_operation == "*":
            curr_total *= curr_num

    return curr_total == total


print(solution("./input.txt"))
