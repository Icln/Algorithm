import sys, heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    t = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        t.append([tmp[1], tmp[2]])
    t.sort()

    end = [t[0][1]]
    for i in range(1, n):
        if t[i][0] >= end[0]:
            heapq.heappop(end)
        heapq.heappush(end, t[i][1])
            
    print(len(end))