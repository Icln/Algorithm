from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    days = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        days.append([a * 100 + b, c * 100 + d])
    days.sort(key=lambda x:(x[0], x[1]))
    days = deque(days)

    start, end = 301, 0
    cnt = 0
    while days:
        if start >= 1201 or start < days[0][0]:
            break
        for _ in range(len(days)):
            if start >= days[0][0]:
                if end <= days[0][1]:
                    end = days[0][1]
                days.popleft()
            else:
                break
        start = end
        cnt += 1

    if start < 1201:
        print(0)
    else:
        print(cnt)