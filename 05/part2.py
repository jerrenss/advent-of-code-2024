import re
from typing import List


def solution(file_name: str) -> int:
    """
    main driver function
    """
    pattern = re.compile(r"^(\d+)\|(\d+)$")
    tracker = set()
    result = 0

    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            match = pattern.match(line)
            if match:
                tracker.add(line)
            elif len(line) == 0:
                continue
            else:
                numbers = line.split(",")
                N = len(numbers)
                terminate = False
                for i in range(N):
                    for j in range(i):
                        if numbers[j] + "|" + numbers[i] not in tracker:
                            numbers[i], numbers[j] = numbers[j], numbers[i]
                            terminate = True
                if terminate:
                    result += int(numbers[int(N/2)])

    return result


print(solution("./input.txt"))
