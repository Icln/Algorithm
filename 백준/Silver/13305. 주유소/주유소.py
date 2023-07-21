import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
p.pop()
result = 0
for i in range(n - 2, -1, -1):
    if p[i] == min(p):
        result += d[i] * p[i]
    else:
        d[i - 1] += d[i]
    p.pop()     
print(result)          