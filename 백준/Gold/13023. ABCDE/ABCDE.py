import sys
input = sys.stdin.readline
def dfs(s):
    if len(tmp) == 5:
        print(1)
        exit()

    for j in arr[s]:
        if not visited[j]:
            visited[j] = 1
            tmp.append(j)
            dfs(j)
            visited[j] = 0
            tmp.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[] for _ in range(n)]

    for i in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(n):
        visited = [0] * n
        tmp = []
        visited[i] = 1
        tmp.append(i)
        dfs(i)

    print(0)