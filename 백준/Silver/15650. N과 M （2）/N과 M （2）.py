import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            dfs(i + 1)
            arr.pop()

dfs(1)

