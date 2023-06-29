import sys
import math
input = sys.stdin.readline
def check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    if n <= 2:
        return 2
    while True:
        if n % 2 == 0:
            n += 1
        else:
            if(check(n)):
                return n
            else :
                n += 1
            
n = int(input())
for _ in range(n):
    print(prime(int(input())))
