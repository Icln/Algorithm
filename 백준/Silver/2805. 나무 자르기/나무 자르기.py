import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    h = (start + end) // 2
    num = 0
    for tree in trees:
        if tree >= h:
            num += (tree - h)
    if num >= m:
        start = h + 1
    else:
        end = h - 1

print(end)