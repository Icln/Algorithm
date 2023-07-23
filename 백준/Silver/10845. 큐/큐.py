import sys
from collections import deque

N=int(input())
queue=deque([])

for i in range(N):
    comd=sys.stdin.readline().split()

    if comd[0]=='push':
        queue.append(int(comd[1]))
    elif comd[0]=='pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif comd[0]=='size':
        print(len(queue))
    elif comd[0]=='empty':
        if queue: print(0)
        else: print(1)
    elif comd[0]=='front':
        if queue: print(queue[0])
        else: print(-1)
    elif comd[0]=='back':
        if queue: print(queue[-1])
        else: print(-1)