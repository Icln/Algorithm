import sys
input = sys.stdin.readline

p = 1000000007
n, k = map(int, input().split())
factorial = [1 for _ in range(n + 1)]

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a % p 
    
    n = power(a, b // 2)
    
    if b % 2: 
        return (n * n * a) % p
    else:
        return (n * n) % p

for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i % p

a = factorial[n]
b = (factorial[n - k] * factorial[k]) % p

print((a % p) * (power(b, p - 2) % p) % p)