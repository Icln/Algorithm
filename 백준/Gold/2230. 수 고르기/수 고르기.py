import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    start, end = 0, 0
    cur = 2000000001
    while start <= end and end < n:
        if arr[end] - arr[start] < m:
            end += 1
        else:
            cur = min(cur, arr[end] - arr[start])
            start += 1
    print(cur)