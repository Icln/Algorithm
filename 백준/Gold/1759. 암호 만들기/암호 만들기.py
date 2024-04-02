import sys
input = sys.stdin.readline

def dfs(idx):
    if len(visited) == l:
        if check(visited):
            result.append(''.join(visited))
        return
    for i in range(idx, c):
        visited.append(alpha[i])
        dfs(i + 1)
        visited.pop()

def check(s):
    tmp = {'a', 'e', 'i', 'o', 'u'}
    cnt = 0
    for i in s:
        if i in tmp:
            cnt += 1

    if cnt >= 1 and l - cnt >= 2:
        return True
    else:
        return False

if __name__ == "__main__":
    l, c = map(int, input().split())
    alpha = list(map(str, input().split()))
    alpha.sort()
    result = []

    visited = []
    dfs(0)
    
    for i in result:
        print(i)