import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
def dfs():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1, n+1):
        arr.append(i)
        dfs()
        arr.pop()

dfs()

