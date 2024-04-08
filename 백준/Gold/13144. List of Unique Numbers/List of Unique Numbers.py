from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    s, e = 0, 0
    cnt = 0
    visited = defaultdict(int)

    while s <= e and e < n:
        if not visited[arr[e]]:
            visited[arr[e]] = 1
            e += 1
            cnt += (e - s)
        else:
            visited[arr[s]] = 0
            s += 1

    print(cnt)
