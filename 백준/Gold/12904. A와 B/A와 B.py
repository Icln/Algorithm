import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = list(input().rstrip())
    t = list(input().rstrip())

    while len(s) != len(t):
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t = t[::-1]
    
    print(1) if s == t else print(0)     