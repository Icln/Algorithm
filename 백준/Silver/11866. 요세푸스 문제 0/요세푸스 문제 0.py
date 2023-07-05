import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

result = []
arr = deque(i+1 for i in range(n))

for i in range(n):
    for j in range(k-1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

print('<', end='')
print(', '.join(map(str,result)), end='')
print('>')