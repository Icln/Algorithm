import sys
input = sys.stdin.readline
def quadTree(n, x, y):
    global result 
    check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != video[i][j]:
                result += '('
                quadTree(n // 2, x, y)
                quadTree(n // 2, x, y + n // 2)
                quadTree(n // 2, x + n // 2, y)
                quadTree(n // 2, x + n // 2, y + n // 2)
                result += ')'
                return
    if check == '1':
        result += '1'
    else:
        result += '0'
    return

n = int(input())
video = [list(map(str,input()))for _ in range(n)]
result = ''
quadTree(n, 0, 0)
print(result)