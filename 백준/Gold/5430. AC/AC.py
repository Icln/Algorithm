import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    instruction = list(input().rstrip())
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    
    flag = True
    R = 0
    if n == 0:
        arr = deque()
    for j in instruction:
        if j == 'R':
            R += 1
        else :
            if len(arr) == 0:
                print('error')
                flag = False
                break
            else:
                if R % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    if flag:
        if R % 2 == 0:
            print('['+','.join(arr)+']')
        else :
            arr.reverse()
            print('['+','.join(arr)+']')
