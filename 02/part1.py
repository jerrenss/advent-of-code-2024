def solution(fileName: str) -> int:
    result: int = 0
    
    with open(fileName, 'r') as file:
        for line in file:
            numbers = line.split()
            N: int = len(numbers)
            i: int = 0
            safe: bool = True
            direction: str = ""
            
            while i < N - 1:
                curr: int = int(numbers[i])
                next: int = int(numbers[i + 1])
                diff: int = curr - next
                if diff == 0:
                    safe = False
                    break
                newDirection: str = getDirection(diff)
                if direction != "" and direction != newDirection:
                    safe = False
                    break
                direction = newDirection
                absDiff = abs(diff)
                if absDiff < 1 or absDiff > 3:
                    safe = False
                    break
                i += 1
            
            if safe:
                result += 1
    
    return result

def getDirection(diff: int) -> str:
    if diff > 0: 
        return "INCR"
    return "DECR"

print(solution("./input.txt"))
