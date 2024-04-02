import sys
input = sys.stdin.readline

def setPrime():
    num = [0] * (n + 1)
    for i in range(2, n + 1):
        if not num[i]:
            prime.append(i)
        for j in range(i * i, n + 1, i):
            num[j] = 1

if __name__ == "__main__":
    n = int(input())
    prime = []
    setPrime()

    l, r = 0, 0
    result = 0
    if len(prime) == 0:
        print(0)
        sys.exit(0)

    cur = prime[0]
    while r <= len(prime):
        if cur <= n:
            if cur == n:
                result += 1
            r += 1
            if r == len(prime):
                break
            cur += prime[r]
        else:
            cur -= prime[l]
            l += 1
    print(result)