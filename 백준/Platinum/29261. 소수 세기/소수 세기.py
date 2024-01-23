from collections import defaultdict
import sys
input = sys.stdin.readline

def check(x, y):
    global result
    if x == 1 or y == 1:
        return
    while True:
        if not prime[x] or not prime[y]:
            x += 1
            y -= 1
        if prime[x] and prime[y]:
            result += 2
            break

    check((x - 1) // 2, (x - 1) - ((x - 1) // 2))
    check((y - 1) // 2, (y - 1) - ((y - 1) // 2))

n = int(input())
prime = defaultdict(bool)
prime[2] = True

for i in range(3, n + 1, 2):
    isPrime = True
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime[i] = True

result = 1
check((n - 1) // 2, (n - 1) - ((n - 1) // 2))
print(result)