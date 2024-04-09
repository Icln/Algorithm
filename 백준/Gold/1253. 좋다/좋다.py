from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0

    for i in range(n):
        tmp = arr[:i] + arr[i+1:]
        cur = arr[i]
        s, e = 0, n - 2
        while s < e:
            if tmp[s] + tmp[e] > cur:
                e -= 1
            elif tmp[s] + tmp[e] < cur:
                s += 1
            else:
                cnt += 1
                break
    print(cnt)
