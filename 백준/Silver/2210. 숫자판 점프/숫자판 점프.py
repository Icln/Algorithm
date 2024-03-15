import sys
from itertools import product
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
num = [list(map(int, input().split())) for _ in range(5)]
result = []

for i in range(5):
    for j in range(5):
        for k in product(range(4), repeat = 5):         
            tmp = []
            tmp.append(num[i][j])
            x, y = i, j
            for z in k:
                x, y = x + dx[z], y + dy[z]
                if not (0 <= x < 5 and 0 <= y < 5):     
                    break
                tmp.append(num[x][y])
            if len(tmp) == 6:
                result.append(''.join(map(str, tmp)))  

print(len(set(result)))