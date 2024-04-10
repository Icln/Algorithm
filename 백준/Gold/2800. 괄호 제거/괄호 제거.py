from itertools import combinations
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = list(map(str, input().rstrip()))
    answer = set()
    stack = []
    tmp = []

    for idx, word in enumerate(n):
        if word == "(":
            stack.append(idx)
        elif word == ")":
            tmp.append((stack.pop(), idx))

    for i in range(1, len(tmp) + 1):
        for j in combinations(tmp, i):
            target = list(n)
            for k in j:
                target[k[0]] = ""
                target[k[1]] = ""

            answer.add(''.join(target))

    for i in sorted(list(answer)):
        print(i)