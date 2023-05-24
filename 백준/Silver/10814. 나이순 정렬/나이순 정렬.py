import sys
input = sys.stdin.readline

arr = []
n = int(input())

for i in range(n):
    [x,y] = input().split()
    arr.append([int(x), y])

arr.sort(key=lambda q : q[0])
for i in range(n):
    print(arr[i][0], arr[i][1])