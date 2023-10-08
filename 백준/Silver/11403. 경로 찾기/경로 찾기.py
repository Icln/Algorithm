import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
    
for k in range(n):
    for i in range(n):
        for j in range(n): 
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in arr:
    for j in i:
        print(j, end = " ")
    print()