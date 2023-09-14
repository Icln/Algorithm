import re
from itertools import permutations
def cal(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    return x * y

def solution(expression):
    operator = set(re.findall("[^0-9]+", expression))
    answer = 0
    for priority in permutations(operator):
        numbers = list(map(int, re.split('[-+*]', expression)))
        operators = re.findall("[^0-9]+", expression)
        
        for op in priority:
            while op in operators:
                idx = operators.index(op)
                tmp = cal(numbers[idx], numbers[idx + 1], op)
                numbers[idx] = tmp
                numbers.pop(idx + 1)
                operators.pop(idx)
            
        answer = max(answer, abs(numbers[0]))        
    return answer