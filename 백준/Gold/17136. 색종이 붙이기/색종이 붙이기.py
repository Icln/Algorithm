import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check(r, c, size):
    for i in range(r, r + size + 1):
        for j in range(c, c + size + 1):
            if arr[i][j] != 1:
                return False
    return True

def detach(r, c, size):
    for i in range(r, r + size + 1):
        for j in range(c, c + size + 1):
            arr[i][j] = 0

def attach(r, c, size):
    for i in range(r, r + size + 1):
        for j in range(c, c + size + 1):
            arr[i][j] = 1


def dfs(r, c, num):
    global result
    if r >= 10:
        result = min(result, num)
        return

    if c >= 10:
        dfs(r + 1, 0, num)
        return

    if arr[r][c] == 1:
        for size in range(5):
            if r + size < 10 and c + size < 10 and check(r, c, size) and cnt[size] > 0:
                cnt[size] -= 1
                detach(r, c, size)
                dfs(r, c + 1, num + 1)
                cnt[size] += 1
                attach(r, c, size)
    else:
        dfs(r, c + 1, num)


if __name__ == "__main__":
    arr = [list(map(int, input().split())) for _ in range(10)]
    cnt = [5, 5, 5, 5, 5]
    result = 26

    dfs(0, 0, 0)
    print(result) if result != 26 else print(-1)
