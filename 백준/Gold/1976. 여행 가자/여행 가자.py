import sys
input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = []
    parents = [i for i in range(n + 1)]
    for i in range(n):
        graph = list(map(int, input().split()))
        for j in range(n):
            if graph[j]:
                union(i + 1, j + 1)

    cities = list(map(int, input().split()))
    start = parents[cities[0]]

    for i in range(1, m):
        if parents[cities[i]] != start:
            print('NO')
            break
    else:
        print('YES')
