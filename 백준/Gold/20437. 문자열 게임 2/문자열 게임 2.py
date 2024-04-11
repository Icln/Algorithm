from collections import defaultdict
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w = input().rstrip()
        k = int(input())

        idx = defaultdict(list)
        for i, val in enumerate(w):
            if w.count(val) >= k:
                idx[val].append(i)

        one, two = 1e9, 0
        for i, j in idx.items():
            l = len(j)
            if l == k:
                tmp = j[-1] - j[0] + 1
                one = min(one, tmp)
                two = max(two, tmp)
            elif l > k:
                s = 0
                e = 0
                while e != len(j) - 1:
                    e = s + (k - 1)
                    one = min(one, j[e] - j[s] + 1)
                    two = max(two, j[e] - j[s] + 1)
                    s += 1

        print(-1) if not two and one > 10000 else print(one, two)
