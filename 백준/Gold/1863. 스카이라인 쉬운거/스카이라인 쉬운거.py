import sys
input = sys.stdin.readline
n = int(input())
buildings = []

for i in range(n):
    x, y = map(int, input().split())
    buildings.append((x, y))

result = 0
tmp = [0]
for i in range(n):
    if tmp[-1] > buildings[i][1]:
        while tmp and tmp[-1] > buildings[i][1]:
            result += 1
            tmp.pop()
    if buildings[i][1] not in tmp:
        tmp.append(buildings[i][1])
print(result + (len(tmp) - 1))
