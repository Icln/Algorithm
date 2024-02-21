import sys
input = sys.stdin.readline

n = int(input())
dpMax, dpMin = [0] * 3, [0] * 3
tmpMax, tmpMin = [0] * 3, [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            tmpMax[j] = a + max(dpMax[0], dpMax[1])
            tmpMin[j] = a + min(dpMin[0], dpMin[1])
            continue
        if j == 1:
            tmpMax[j] = b + max(dpMax[0], dpMax[1], dpMax[2])
            tmpMin[j] = b + min(dpMin[0], dpMin[1], dpMin[2])
            continue
        if j == 2:
            tmpMax[j] = c + max(dpMax[1], dpMax[2])
            tmpMin[j] = c + min(dpMin[1], dpMin[2])
            continue
    for j in range(3):
        dpMax[j] = tmpMax[j]
        dpMin[j] = tmpMin[j]

print(max(dpMax), min(dpMin))