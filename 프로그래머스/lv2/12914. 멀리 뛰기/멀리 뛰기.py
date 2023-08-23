import math
def solution(n):
    answer = 1
    for two in range(1, (n // 2) + 1):
        one = n - (2 * two)
        answer += (math.factorial(one + two) // (math.factorial(one) * math.factorial(two)))     
    return answer % 1234567