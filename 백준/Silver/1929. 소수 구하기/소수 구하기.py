import sys
import math
input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else: 
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True
    
x, y = map(int, input().split())
for i in range(x, y+1):
    if prime(i):
        print(i)