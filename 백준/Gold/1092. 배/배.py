import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
else:
    visited = [False] * m
    result = 0
    while True:
        cnt = 0
        idx = 0
        for i in range(m):
            if len(cranes) == idx:
                break
            if not visited[i] and cranes[idx] >= boxes[i]:
                idx += 1
                cnt += 1
                visited[i] = True

        result += 1
        if len(set(visited)) == 1 and visited[0]:
            break
    print(result)