import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(i + 1 for i in range(n))
while len(queue) > 1 :
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])