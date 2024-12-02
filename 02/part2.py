from typing import List

def solution(fileName: str) -> int:
    result = 0
    
    with open(fileName, 'r') as file:
        for line in file:
            numbers = line.split()
            if isSafe(numbers):
                result += 1
                continue
            otherLists = generateLists(numbers)
            for otherList in otherLists:
                if isSafe(otherList):
                    result += 1
                    break
    return result

def generateLists(inputList: List[str]) -> List[List[str]]:
    output = []
    for i in range(len(inputList)):
        subList = inputList[:i] + inputList[i+1:]
        output.append(subList)
    return output

def isSafe(inputList: List[str]) -> bool:
    N = len(inputList)
    i = 0
    safe = True
    direction = ""
    
    while i < N - 1:
        curr = int(inputList[i])
        next = int(inputList[i + 1])
        diff = curr - next
        if diff == 0:
            safe = False
            break
        newDirection = getDirection(diff)
        if direction != "" and direction != newDirection:
            safe = False
            break
        direction = newDirection
        absDiff = abs(diff)
        if absDiff < 1 or absDiff > 3:
            safe = False
            break
        i += 1
    
    return safe

def getDirection(diff: int) -> str:
    if diff > 0: 
        return "INCR"
    return "DECR"

print(solution("./input.txt"))
