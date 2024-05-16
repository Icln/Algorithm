import sys, re
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    p = re.compile('(100+1+|01)+')
    print("SUBMARINE") if p.fullmatch(s) else print("NOISE")