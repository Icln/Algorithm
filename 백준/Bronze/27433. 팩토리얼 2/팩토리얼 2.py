import sys
input = sys.stdin.readline

def factorial(x):
    if x == 0 :
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(int(input())))