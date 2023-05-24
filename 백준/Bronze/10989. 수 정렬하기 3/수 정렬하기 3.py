import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001

for i in range(n):
    num = int(input())    
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)