import heapq
import sys
input = sys.stdin.readline

for i in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    result = 0
    while len(arr) >= 2:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        result += (first + second)
        heapq.heappush(arr, (first + second))
    print(result)