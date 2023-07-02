import sys
import math
input = sys.stdin.readline
def checkPrime(x):
    if x < 2:
        return False
    elif x == 2 :
        return True
    elif x % 2 == 0:
        return False
    else :
        for i in range(3,int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True


def numPrime(x):
    result = 0
    for i in range(x + 1, 2 * x +1):
        if checkPrime(i):
            result += 1
    return result


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(numPrime(n))
