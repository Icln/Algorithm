import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    p = input().rstrip()

    tmp, result = 0, 0
    for i in range(1, len(p)):
        if s.find(p[tmp:i + 1]) == -1:
            tmp = i
            result += 1
    print(result + 1)