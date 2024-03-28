from collections import defaultdict
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    M = 10000000
    tmp = [0] * (M + 1)
    prime = []
    isPrime = defaultdict(int)
    for i in range(2, M + 1):
        if not tmp[i]:
            prime.append(i)
            isPrime[i] = 1
            for j in range(i * i, M + 1, i):
                tmp[j] = 1

    for t in range(1, int(input()) + 1):
        m = int(input())
        n = list(map(int, input().split()))
        visited = defaultdict(int)

        flag, result = False, 0
        for i in range(0, len(prime)):
            for j in range(m):
                s = sum(prime[i: i + n[j]])
                if isPrime[s]:
                    visited[s] += 1
                    if visited[s] == m:
                        flag = True
                        result = s
                        break
            if flag:
                print(f"Scenario {t}:")
                print(result)
                print()
                break
