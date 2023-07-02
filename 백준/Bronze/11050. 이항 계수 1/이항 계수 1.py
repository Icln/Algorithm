import sys
input = sys.stdin.readline
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) 

n, k  = map(int, input().split())
print(factorial(n) // (factorial(k)*factorial(n-k)))
