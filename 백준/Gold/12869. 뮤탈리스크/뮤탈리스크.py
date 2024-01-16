from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split())) + (3 - n) * [0]
cases = list(permutations([9, 3, 1], 3))
visited = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
visited[scv[0]][scv[1]][scv[2]] = 0
q = deque([[scv[0], scv[1], scv[2]]])

while q:
    hp = q.popleft()
    if hp[0] == 0 and hp[1] == 0 and hp[2] == 0:
        print(visited[hp[0]][hp[1]][hp[2]])
        break

    for case in cases:
        tmp = [max(hp[0] - case[0], 0), max(hp[1] - case[1], 0), max(hp[2] - case[2], 0)]
        if visited[tmp[0]][tmp[1]][tmp[2]] == -1:
            visited[tmp[0]][tmp[1]][tmp[2]] = visited[hp[0]][hp[1]][hp[2]] + 1
            q.append(tmp)