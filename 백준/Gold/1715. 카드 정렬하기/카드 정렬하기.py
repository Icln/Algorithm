import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
heapq.heapify(arr)

result = 0
while len(arr) != 1:
    x = arr[0]
    heapq.heappop(arr)
    y = arr[0]
    heapq.heappop(arr)
    result += (x+y)
    heapq.heappush(arr, x+y)

print(result)