import sys
input = sys.stdin.readline

def solve(arr, x):
    mid = (len(arr) // 2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    solve(arr[:mid], x + 1)
    solve(arr[mid + 1:], x + 1)

    
k = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(k)]
solve(arr, 0)
for i in range(k):
    print(*tree[i])