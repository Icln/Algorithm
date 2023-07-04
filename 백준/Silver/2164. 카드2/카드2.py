import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(i + 1 for i in range(n))
cnt = 1
while len(queue) != 1 :
    if cnt % 2 == 1:
        queue.popleft()
        cnt += 1
    else :
        queue.append(queue[0])
        queue.popleft()
        cnt += 1

print(queue[0])