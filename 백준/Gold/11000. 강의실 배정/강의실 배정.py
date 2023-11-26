import heapq
import sys
input = sys.stdin.readline
n = int(input())
times = []

for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times.sort()
room = []
heapq.heappush(room, times[0][1])

for i in range(1, n):
    if times[i][0] < room[0]:
        heapq.heappush(room, times[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, times[i][1])

print(len(room))
