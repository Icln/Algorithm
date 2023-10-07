import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
dis = [sys.maxsize] * 100001
dis[n] = 0

queue = []
heapq.heappush(queue, [n, 0])
while queue:
    pos, cur = heapq.heappop(queue)
    for i in ([pos - 1, 1], [pos + 1, 1], [pos * 2, 0]):
        if 0 <= i[0] < 100001 and dis[i[0]] > cur + i[1]:
            dis[i[0]] = cur + i[1]
            heapq.heappush(queue, [i[0], dis[i[0]]])

print(dis[k])