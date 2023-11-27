import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
arr.sort(key=lambda x: x[0])
mid = round(sum(i[1] for i in arr)/2)

cnt = 0
for i in arr:
    cnt += i[1]

    if cnt >= mid:
        print(i[0])
        break