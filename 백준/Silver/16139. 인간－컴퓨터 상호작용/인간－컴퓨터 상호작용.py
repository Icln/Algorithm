import sys
input = sys.stdin.readline

s = list(input().rstrip())
n = int(input())

arr = [[0 for _ in range(26)] for _ in range(len(s))]

for i in range(len(s)):
    for j in range(26):
        if ord(s[i]) - 97 == j:
            arr[i][j] = arr[i-1][j] + 1
        else:
            arr[i][j] = arr[i-1][j]


for i in range(n):
    a, start, end = input().split()
    if int(start) == 0:
        print(arr[int(end)][ord(a) - 97])
    else:
        print(arr[int(end)][ord(a) - 97] - arr[int(start) - 1][ord(a) - 97]) 