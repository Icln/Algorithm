import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and arr[nx] == 0:
                arr[nx] = arr[x] + 1
                queue.append(nx)
    return arr[k]

n, k = map(int, input().split())
arr = [0] * (100001)
print(bfs())
