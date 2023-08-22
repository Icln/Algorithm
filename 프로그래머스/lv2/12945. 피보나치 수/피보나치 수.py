def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, (a+b) % 1234567
    return a