import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int,input().split()))
for i in range(n - 1):
    arr[i + 1] += arr[i]
arr = [0] + arr

for _ in range(m):
    start, end = map(int,input().split())
    print(arr[end] - arr[start -1])