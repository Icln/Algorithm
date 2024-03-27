from collections import deque, defaultdict
import sys
input = sys.stdin.readline
def bfs(s):
    q = deque([(s)])
    visited = defaultdict(int)
    idx = defaultdict(int)
    visited[s] = 1
    tmp, j = 1, 0
    while q:
        x = q.popleft()
        if not visited[arr[x]] and cnt[arr[x]]:
            return 0
        if visited[arr[x]]:
            return tmp - idx[arr[x]]
        j += 1
        tmp += 1
        idx[arr[x]] = j
        cnt[arr[x]] = 1
        visited[arr[x]] = 1
        q.append(arr[x])

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [0] + list(map(int, input().split()))
        cnt = defaultdict(int)
        result = 0
        for i in range(1, n + 1):
            if not cnt[arr[i]]:
                cnt[i] = 1
                result += bfs(i)
            cnt[i] = 1

        print(n - result)
