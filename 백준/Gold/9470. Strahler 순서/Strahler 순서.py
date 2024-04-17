from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        k, m, p = map(int, input().split())
        arr = [[] for _ in range(m + 1)]

        indgree = [0] * (m + 1)
        cnt = [[0, 0]] * (m + 1)
        order = [0] * (m + 1)
        for _ in range(p):
            a, b = map(int, input().split())
            arr[a].append(b)
            indgree[b] += 1

        q = deque()
        for j in range(1, m + 1):
            if indgree[j] == 0:
                cnt[j] = [1, 1]
                q.append(j)

        while q:
            cur = q.popleft()
            if cnt[cur][1] >= 2:
                order[cur] = cnt[cur][0] + 1
            else:
                order[cur] = cnt[cur][0]

            for j in arr[cur]:
                indgree[j] -= 1
                if cnt[j][0] == order[cur]:
                    cnt[j][1] += 1
                elif cnt[j][0] < order[cur]:
                    cnt[j] = [order[cur], 1]

                if indgree[j] == 0:
                    q.append(j)

        print(i, order[m])