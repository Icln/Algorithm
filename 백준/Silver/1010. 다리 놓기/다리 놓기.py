import sys
input = sys.stdin.readline
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) 

for i in range(int(input())):
    n, k  = map(int, input().split())
    if n > k:
        print(factorial(n) // (factorial(k)*factorial(n-k)))
    else :
        print(factorial(k) // (factorial(n)*factorial(k-n)))
        