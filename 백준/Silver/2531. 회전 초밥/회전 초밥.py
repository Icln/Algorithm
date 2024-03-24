import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input())for _ in range(n)]
l, r = 0, k
answer = 0
while l < n:
  s = set()
  for i in range(l, r):
    s.add(sushi[i % n])
  if c not in s:
    s.add(c)

  answer = max(answer, len(s))
  l += 1
  r += 1

print(answer)