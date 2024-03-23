from collections import defaultdict
import sys
input = sys.stdin.readline
n, p, q = map(int, input().split())
dict = defaultdict(int)
dict[0] = 1

def solve(x):
    if dict[x]:
        return dict[x]
    else:
        dict[x] = solve(x//p) + solve(x//q)
        return dict[x]

print(solve(n))