import sys
input = sys.stdin.readline

if __name__ == "__main__":
    g = int(input())
    x, y = 1, 1
    result = []
    while True:
        diff = y ** 2 - x ** 2
        if y - x == 1 and diff > g:
            break

        if diff > g:
            x += 1
        elif diff < g:
            y += 1
        else:
            result.append(y)
            x += 1
            y += 1

    if result:
        print(*result, sep='\n')
    else:
        print(-1)
