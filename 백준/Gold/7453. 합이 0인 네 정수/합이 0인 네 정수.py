import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    A, B, C, D = [], [], [], []
    for i in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    AB, CD = [], []
    for a in A:
        for b in B:
           AB.append(a + b)
    for c in C:
        for d in D:
           CD.append(c + d)

    AB.sort()
    CD.sort()

    l, r = 0, len(CD) - 1
    cnt = 0
    while l < len(AB) and r >= 0:
        cur = AB[l] + CD[r]
        if cur == 0:
            tmpL, tmpR = l + 1, r - 1
            while tmpL < len(AB) and AB[l] == AB[tmpL]:
                tmpL += 1
            while tmpR >= 0 and CD[r] == CD[tmpR]:
                tmpR -= 1
            cnt += (tmpL - l) * (r - tmpR)
            l, r = tmpL, tmpR
        
        elif cur < 0:
            l += 1
        else:
            r -= 1

    print(cnt)