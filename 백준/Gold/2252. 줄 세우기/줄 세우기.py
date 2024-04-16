import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    indgree = [0] * (n + 1)
    arr = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        indgree[b] += 1
        arr[a].append(b)

    stack = []
    for i in range(1, n + 1):
        if indgree[i] == 0:
            stack.append(i)

    result = []
    while stack:
        cur = stack.pop()
        result.append(cur)
        for i in arr[cur]:
            indgree[i] -= 1
            if indgree[i] == 0:
                stack.append(i)

    print(*result)