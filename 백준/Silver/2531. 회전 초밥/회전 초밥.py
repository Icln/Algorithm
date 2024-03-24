import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)] * 2
cnt = 0
for i in range(n):
    s = set(sushi[i : i + k])
    s.add(c)
    cnt = max(cnt, len(s))
print(cnt)