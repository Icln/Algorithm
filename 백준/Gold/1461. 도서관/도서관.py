import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    dis = []

    for i in range(0, len(pos), m):
        dis.append(pos[i])
    for i in range(len(neg) - 1, -1, -m):
        dis.append(abs(neg[i]))

    dis.sort()
    print(sum(dis[:-1]) * 2 + dis[-1])