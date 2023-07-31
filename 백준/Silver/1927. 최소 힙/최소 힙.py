import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(arr, x)
    else:
        try:
            print(heapq.heappop(arr))
        except:
            print(0)