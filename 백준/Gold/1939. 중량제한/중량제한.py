from collections import deque
import sys
input = sys.stdin.readline
MAX = 1000000000


def bfs(limit):
    q = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    while q:
        cur = q.popleft()

        for next, weight in graph[cur]:
            if not visited[next] and weight >= limit:
                visited[next] = 1
                q.append(next)

    return True if visited[end] else False

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] * (m + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    start, end = map(int, input().split())

    left, right = 0, MAX
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid):
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    print(result)