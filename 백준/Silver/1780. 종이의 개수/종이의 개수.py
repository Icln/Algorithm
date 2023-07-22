import sys
input = sys.stdin.readline
def divide(n, x, y):
    global minus, zero, one 
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                divide(n // 3, x, y)
                divide(n // 3, x, y + n // 3)
                divide(n // 3, x, y + (n // 3) * 2)
                
                divide(n // 3, x + n // 3, y)
                divide(n // 3, x + n // 3, y + n // 3)
                divide(n // 3, x + n // 3, y + (n // 3) * 2)
                
                divide(n // 3, x + (n // 3) * 2, y)
                divide(n // 3, x + (n // 3) * 2, y + n // 3)
                divide(n // 3, x + (n // 3) * 2, y + (n // 3) * 2)
                return
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        one += 1
    return

n = int(input())
paper = [list(map(int,input().split()))for _ in range(n)]
minus, zero, one = 0, 0, 0
divide(n, 0, 0)

print(minus)
print(zero)
print(one)