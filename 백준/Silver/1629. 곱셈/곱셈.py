import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % c
    
    n = power(a, b//2)
    if b % 2 == 0:
        return (n * n) % c
    else:
        return (n * n * a) % c
print((power(a,b))%c)
