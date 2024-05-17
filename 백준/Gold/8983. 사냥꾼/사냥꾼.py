import sys
input = sys.stdin.readline

if __name__ == "__main__":
    m, n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    animal = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    ans = 0

    for a, b in animal:
        if b > l:
            continue
        MIN, MAX = a + b - l, a - b + l
        s, e = 0, m - 1
        while s <= e:
            mid = (s + e) // 2
            if MIN <= arr[mid] <= MAX:
                ans += 1
                break
            elif arr[mid] < MAX:
                s = mid + 1
            else:
                e = mid - 1
    print(ans)