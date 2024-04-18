from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cost = [0] * (n + 1)
    arr = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(1, n + 1):
        time, *tmp = map(int, input().split())
        cost[i] = time
        for j in tmp:
            if j == -1:
                break
            arr[j].append(i)
            indegree[i] += 1

    q = deque()
    for j in range(1, n + 1):
        if indegree[j] == 0:
            q.append(j)

    result = [0] * (n + 1)
    while q:
        cur = q.popleft()
        result[cur] += cost[cur]
        for j in arr[cur]:
            indegree[j] -= 1
            result[j] = max(result[j], result[cur])
            if indegree[j] == 0:
                q.append(j)

    for i in range(1, n + 1):
        print(result[i])