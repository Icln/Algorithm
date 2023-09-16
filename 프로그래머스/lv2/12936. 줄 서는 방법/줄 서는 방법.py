from math import factorial
def solution(n, k):
    answer = []
    number = [i for i in range(1, n + 1)]
    while not n == 0:
        num = factorial(n) // n
        idx = k // num if k % num else k // num - 1

        answer.append(number.pop(idx))
        n, k = n - 1, k % num

    return answer