import sys
input = sys.stdin.readline
n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
if cranes[0] < boxes[0]:
    print(-1)
else:
    result = 0
    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        result += 1
    print(result)
