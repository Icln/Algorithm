from collections import deque

for i in range(10):
    n = int(input())
    arr = deque(list(map(int, input().split())))
    flag = False

    while not flag:
        for j in range(1, 6):
            if min(arr) <= 0:
                flag = True
                break
            if arr[0] - j < 0:
                arr.popleft()
                arr.append(0)
            else:
                arr.append(arr.popleft() - j) 
    print(f'#{n}', *arr)
    