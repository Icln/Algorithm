import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        arr = list(map(int, input().split()))
        answer = 0
        cur = sum(arr[:m])
        if cur < k:
            answer = 1
        if n == m:
            print(answer)
            continue
        else:
            for i in range(m - 1):
                arr.append(arr[i])

        l, r = 0, m
        while l < n - 1:
            cur -= arr[l]
            cur += arr[r]
            l += 1
            r += 1
            if cur < k:
                answer += 1

        print(answer)