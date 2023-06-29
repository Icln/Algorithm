import sys
import math
input = sys.stdin.readline

def check(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    else:
        if (check(x)):
            return True
        else:
            return False
x, y = map(int, input().split())

for i in range(x, y+1):
    if(prime(i)):
        print(i)