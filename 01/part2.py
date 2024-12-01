from typing import Dict, List

def solution(fileName: str) -> int:
    rightMap: Dict[int, int] = {}
    leftList: List[int] = []
    result: int = 0
    
    with open(fileName, 'r') as file:
        for line in file:
            numbers = line.split()
            leftList.append(numbers[0])

            rightKey: int = int(numbers[1])
            if rightKey not in rightMap:
                rightMap[rightKey] = 1
            else: 
                rightMap[rightKey] += 1
        
        for n in leftList:
            count: int = rightMap.get(int(n), 0)
            result += int(n) * count
    
    return result

print(solution("./input.txt"))