import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(start, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()

dfs(1)

