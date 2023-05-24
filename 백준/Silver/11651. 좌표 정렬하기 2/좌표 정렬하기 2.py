import sys
input = sys.stdin.readline

arr = []
n = int(input())

for i in range(n):
    [a, b] = map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda l: (l[1], l[0]))
for i in range(n):
    print(arr[i][0], arr[i][1])
