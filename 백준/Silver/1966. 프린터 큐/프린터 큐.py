import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    n,m = map(int, input().split())
    queue = deque(list(map(int,input().split())))
    result = 0
    
    while queue:
        biggest = max(queue)
        first = queue.popleft()
        m -= 1
        
        if biggest == first:
            result += 1
            if m < 0 :
                print(result)
                break
        else:
            queue.append(first)
            if m < 0:
                m = len(queue) - 1