from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def bfs(s):
    q = deque([(s)])
    visited[s] = 1
    while q:
        cur = q.popleft()
        for idx, next in enumerate(graph[cur]):
            if next and not visited[idx]:
                visited[idx] = 1
                q.append(idx)


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    cities = list(map(int, input().split()))
    visited = defaultdict(int)
    bfs(cities[0] - 1)

    flag = True
    for city in cities:
        if not visited[city - 1]:
            flag = False

    print('YES') if flag else print('NO')