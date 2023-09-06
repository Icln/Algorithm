from itertools import permutations
answer = 0
def isPrime(x):
    global answer
    if x <= 1:
        return
    if x == 2:
        answer += 1
        return
    if x % 2 == 0:
        return
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return
    answer += 1

def solution(numbers):
    candidate = set()
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            candidate.add(int(''.join(j)))
    
    for i in candidate:
        isPrime(i)        
    return answer