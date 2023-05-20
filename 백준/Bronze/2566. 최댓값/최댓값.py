import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int,input().split())))

MAX = -1
for i in range(9):
    for j in range(9):
        if arr[i][j] > MAX:
            MAX = arr[i][j]
            x = i + 1
            y = j + 1

print(MAX)
print(x, y)