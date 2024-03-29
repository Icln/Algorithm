import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    l, r = 0, 0
    cur = 0
    result = 1e9
    while True:
        if cur >= s:
            result = min(result, r - l)
            cur -= arr[l]
            l += 1
        elif r == n:
            break
        else:
            cur += arr[r]
            r += 1
    print(0) if result == 1e9 else print(result)