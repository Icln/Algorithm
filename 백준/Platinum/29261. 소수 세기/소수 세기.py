from collections import defaultdict
import sys
input = sys.stdin.readline

def check(x, y):
    global result
    if x == 1 or y == 1:
        return
    while True:
        if prime[x] or prime[y]:
            x += 1
            y -= 1
        if not prime[x] and not prime[y]:
            result += 2
            break

    check((x - 1) // 2, (x - 1) - ((x - 1) // 2))
    check((y - 1) // 2, (y - 1) - ((y - 1) // 2))

n = int(input())
prime = defaultdict(bool)

for i in range(2, int(n ** 0.5) + 1):
    for j in range(i * 2, n + 1, i):
        prime[j] = True

result = 1
check((n - 1) // 2, (n - 1) - ((n - 1) // 2))
print(result)