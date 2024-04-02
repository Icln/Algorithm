import sys, heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n, m, l = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [l]
    arr.sort()

    diff = []
    for i in range(1, n + 2):
        heapq.heappush(diff, (-(arr[i] - arr[i - 1]), 1))

    for _ in range(m):
        dist, cnt = heapq.heappop(diff)
        dist = -dist * cnt
        heapq.heappush(diff, (-dist / (cnt + 1), cnt + 1))

    result = -heapq.heappop(diff)[0]
    print(int(result)) if result == int(result) else print(int(result) + 1)