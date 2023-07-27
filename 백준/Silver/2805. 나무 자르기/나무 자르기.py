import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))
start, end = 1, trees[-1]

while start <= end:
    h = (start + end) // 2
    num = 0
    for tree in trees:
        if tree > h:
            num += (tree - h)
        if num > m:
            break

    if num >= m:
        start = h + 1
    else:
        end = h - 1
    
print(end)