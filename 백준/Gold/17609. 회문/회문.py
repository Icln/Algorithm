import sys
input = sys.stdin.readline


def check(l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    for _ in range(int(input())):
        s = input().rstrip()
        l, r = 0, len(s) - 1
        cnt = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if check(l + 1, r) or check(l, r - 1):
                    cnt = 1
                else:
                    cnt = 2
                break
        print(cnt)