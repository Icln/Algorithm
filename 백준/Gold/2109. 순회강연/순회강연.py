import sys, heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])

    q = []
    for i in arr:
        p, d = i
        heapq.heappush(q, p)
        if len(q) > d:
            heapq.heappop(q)

    print(sum(q))