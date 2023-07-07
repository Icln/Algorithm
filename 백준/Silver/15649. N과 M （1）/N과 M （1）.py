import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
for num in permutations(arr, m):
    print(' '.join(str(i) for i in num))