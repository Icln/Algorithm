from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        d = [0] + list(map(int, input().split()))
        arr = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        dp = [0] * (n + 1)

        for _ in range(k):
            a, b = map(int, input().split())
            arr[a].append(b)
            indegree[b] += 1

        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = d[i]

        while q:
            cur = q.popleft()
            for i in arr[cur]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[cur] + d[i])
                if indegree[i] == 0:
                    q.append(i)

        print(dp[int(input())])