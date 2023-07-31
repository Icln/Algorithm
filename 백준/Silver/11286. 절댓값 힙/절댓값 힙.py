import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x:
        if x > 0:
            heapq.heappush(arr, (x, x))
        else:
            heapq.heappush(arr, (-x, x))
    else:
        try:
            print(heapq.heappop(arr)[1])
        except:
            print(0)