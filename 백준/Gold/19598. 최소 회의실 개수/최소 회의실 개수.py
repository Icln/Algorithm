import heapq
import sys
input = sys.stdin.readline
n = int(input())
times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort(key = lambda x:x[0])
rooms = []
heapq.heappush(rooms, times[0][1])
for i in range(1, n):
    if rooms[0] > times[i][0]:
        heapq.heappush(rooms, times[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, times[i][1])

print(len(rooms))