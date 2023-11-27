import sys
input = sys.stdin.readline
def change(cur, want):
    cnt = 0
    for i in range(1, n):
        if cur[i - 1] == want[i - 1]:
            continue

        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                cur[j] = 1 - cur[j]

    return cnt if cur == want else sys.maxsize

n = int(input())
cur = list(map(int, input().rstrip()))
want = list(map(int, input().rstrip()))

answer = change(cur[:], want)

cur[0] = 1 - cur[0]
cur[1] = 1 - cur[1]
answer = min(answer, change(cur[:], want) + 1)
print(answer if answer != sys.maxsize else -1)
