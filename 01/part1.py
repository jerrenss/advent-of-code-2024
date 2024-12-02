from typing import List

def solution(fileName: str) -> int:
    leftList: List[int] = []
    rightList: List[int] = []
    
    with open(fileName, 'r') as file:
        for line in file:
            numbers = line.split()
            leftList.append(numbers[0])
            rightList.append(numbers[1])

    leftList.sort()
    rightList.sort()
    
    N: int = len(leftList)
    result: int = 0
    for i in range(N):
        result += abs(int(leftList[i]) - int(rightList[i]))

    return result

print(solution("./input.txt"))
