from itertools import *

n, m = map(int,input().split())
arr = list(map(int,input().split()))

s = [sum(c) for c in combinations(arr,3) if sum(c) <= m]
print(max(s))
