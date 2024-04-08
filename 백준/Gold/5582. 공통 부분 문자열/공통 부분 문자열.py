import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    t = input().rstrip()

    if len(s) > len(t):
        s, t = t, s

    start, end, result = 0, 0, 0
    while start <= end < len(s):
        if s[start: end + 1] in t:
            result = max(result, end - start + 1)
        else:
            start += 1
        end += 1

    print(result)
