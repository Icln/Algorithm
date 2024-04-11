from itertools import combinations
from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    if k < 5:
        print(0)
        sys.exit(0)

    cnt = defaultdict(int)
    d = {'a', 'c', 'i', 't', 'n'}
    alpha = [chr(97 + i) for i in range(26) if chr(97 + i) not in d]
    for i in d:
        cnt[i] = 1

    strings = [input().rstrip() for _ in range(n)]
    result = 0
    for a in combinations(alpha, k - 5):
        tmp = cnt.copy()
        for i in a:
            tmp[i] = 1

        ans = 0
        for s in strings:
            sub = s[4:-4]
            flag = True
            for i in sub:
                if tmp[i] == 0:
                    flag = False
                    break
            if flag:
                ans += 1

        result = max(result, ans)
    print(result)