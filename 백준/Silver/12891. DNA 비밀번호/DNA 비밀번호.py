from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s, p = map(int, input().split())
    tmp = list(input().rstrip())
    a, c, g, t = map(int, input().split())
    cnt = defaultdict(int)
    result = 0

    for i in range(p):
        cnt[tmp[i]] += 1

    if cnt['A'] >= a and cnt['C'] >= c and cnt['G'] >= g and cnt['T'] >= t:
        result += 1

    s, e = 0, p
    for i in range(len(tmp) - p):
        cnt[tmp[s + i]] -= 1
        cnt[tmp[e + i]] += 1    
        if cnt['A'] >= a and cnt['C'] >= c and cnt['G'] >= g and cnt['T'] >= t:
            result += 1

    print(result)
