import sys
input = sys.stdin.readline

def check():
    cnt = 0
    for word in words:
        flag = True
        for s in word:
            if not alpha[ord(s) - 97]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt


def dfs(start, depth):
    global ans

    if depth == k:
        ans = max(ans, check())
        return

    for i in range(start, 26):
        if not alpha[i]:
            alpha[i] = True
            dfs(i, depth + 1)
            alpha[i] = False

if __name__ == '__main__':
    n, k = map(int, input().split())
    alpha = [False for _ in range(26)]
    words = [input().rstrip() for _ in range(n)]
    ans = 0

    if k < 5:
        print(0)
    elif k == 26:
        print(n)
    else:
        for c in ('a', 'c', 'i', 'n', 't'):
            alpha[ord(c) - ord('a')] = True

        dfs(0, 5)
        print(ans)