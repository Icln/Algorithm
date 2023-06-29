import sys
input = sys.stdin.readline

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x,y)

n = int(input().strip())

for _ in range(n):
    x ,y = map(int, input().strip().split())
    print(lcm(x, y))
