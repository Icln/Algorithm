from itertools import permutations
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))
def rotate(size, xs, xe, ys, ye):
    if size < 2:
        return
    
    p1, p2, p3 = tmp[xs][ye], tmp[xe][ye], tmp[xe][ys]
    for y in range(ye, ys, -1):
        tmp[xs][y] = tmp[xs][y - 1]
    for x in range(xe, xs + 1, -1):
        tmp[x][ye] = tmp[x - 1][ye]
    for y in range(ys, ye - 1):
        tmp[xe][y] = tmp[xe][y + 1]
    for x in range(xs, xe - 1,):
        tmp[x][ys] = tmp[x + 1][ys]

    tmp[xs + 1][ye], tmp[xe][ye - 1], tmp[xe - 1][ys] = p1, p2, p3
    rotate(size - 2, xs + 1, xe - 1, ys + 1, ye - 1)

n, m, k = map(int, input().split())
arr = [[0]] + [[0] + list(map(int, input().split())) for _ in range(n)]
spin = []
for _ in range(k):
    r, c, s = map(int, input().split())
    spin.append((r - s, c - s, r + s, c + s))

result = 1e9
for permutation in permutations(spin, k):
    tmp = copy.deepcopy(arr)
    for i in permutation:
        rotate(i[2] - i[0] + 1, i[0], i[2], i[1], i[3])
    for i in range(1, n + 1):
        result = min(result, sum(tmp[i]))

print(result)