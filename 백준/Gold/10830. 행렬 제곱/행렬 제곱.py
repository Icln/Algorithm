import sys
input = sys.stdin.readline

def mul(m1, m2):
    temp = [[0 for _ in range(n)]for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += m1[i][k] * m2[k][j]
            temp[i][j] %= 1000
    return temp

def matrix(arr, b):
    if b == 1:
       return arr 

    tmp = matrix(arr, b // 2)
    if b % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp,tmp), arr)

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = matrix(arr, b)

for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end = ' ')
    print()