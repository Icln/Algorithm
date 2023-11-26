import sys
input = sys.stdin.readline
n = int(input())
buildings = []

for i in range(n):
    x, y = map(int, input().split())
    buildings.append((x, y))

result = 0
tmp = []
for i in range(n):
    if tmp and tmp[-1] > buildings[i][1]:
        if buildings[i][1] == 0:
            result += len(tmp)
            tmp = []
        else:
            while tmp and tmp[-1] > buildings[i][1]:
                result += 1
                tmp.pop()
    if buildings[i][1] != 0 and buildings[i][1] not in tmp:
        tmp.append(buildings[i][1])

print(result + len(tmp))
