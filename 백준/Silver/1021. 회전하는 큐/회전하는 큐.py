import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque([i + 1 for i in range(n)])
idx = list(map(int, input().split()))
result = 0

for i in idx:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue)//2:
                queue.rotate(-1)
                result += 1
            else:
                queue.rotate(1)
                result += 1
print(result)
