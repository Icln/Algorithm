import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    p, m = [], []
    result = 0
    for _ in range(n):
        tmp = int(input())
        if tmp > 1:
            p.append(tmp)
        elif tmp <= 0:
            m.append(tmp)
        else:
            result += tmp

    p.sort(reverse=True)
    m.sort()

    for i in range(0, len(p), 2):
        if i + 1 >= len(p):
            result += p[i]
        else:
            result += (p[i] * p[i + 1])

    for i in range(0, len(m), 2):
        if i + 1 >= len(m):
            result += m[i]
        else:
            result += (m[i] * m[i + 1])
    print(result)