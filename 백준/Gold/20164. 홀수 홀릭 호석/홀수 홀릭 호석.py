import sys
input = sys.stdin.readline

def count_odd(n):
    cnt = 0
    for i in n:
        if int(i) & 1:
            cnt += 1
    return cnt


def divided(n, cnt):
    global max_v, min_v
    s = str(n)
    cnt += count_odd(s)

    if len(s) == 1:
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return
    elif len(s) == 2:
        divided(n // 10 + n % 10, cnt)
    else:
        for i in range(1, len(s) - 1):
            for j in range(i + 1, len(s)):
                new_num = int(s[:i]) + int(s[i: j]) + int(s[j:])
                divided(new_num, cnt)

n = int(input())
min_v = float('inf')
max_v = 0

divided(n, 0)

print(min_v, max_v)