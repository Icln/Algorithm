from collections import deque
import copy
def bfs(start, tmp):
    queue = deque()
    queue.append(start)
    cnt = 0
    while queue:
        x = queue.popleft()
        cnt += 1
        for i in range(len(tmp)):
            if x == tmp[i][0]:
                queue.append(tmp[i][1])
                tmp[i][0], tmp[i][1] = -1, -1
            elif x == tmp[i][1]:
                queue.append(tmp[i][0])
                tmp[i][0], tmp[i][1] = -1, -1
    return cnt

def solution(n, wires):
    answer = 10 ** 9
    for i in range(len(wires)):
        arr = copy.deepcopy(wires)
        arr.remove(wires[i])
        answer = min(answer, abs(bfs(wires[i][0], arr) - bfs(wires[i][1], arr)))
    return answer