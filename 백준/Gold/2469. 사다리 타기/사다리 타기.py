import sys
input = sys.stdin.readline

if __name__ == "__main__":
    k = int(input())
    n = int(input())
    arr = list(map(str, input().rstrip()))
    s = sorted(arr)
    mid = 0
    ladder = [[[0, '*']] * k for _ in range(n)]
    for i in range(n):
        tmp = list(map(str, input().rstrip()))
        for j in range(k - 1):
            if tmp[j] == '-':
                ladder[i][j], ladder[i][j + 1] = [1, '-'], [1, '*']
            elif tmp[j] == '?':
                ladder[i][j], ladder[i][j + 1] = '?', '?'
                mid = i

    up, down = [0] * k, [0] * k
    for i in range(k):
        tmp = i
        for j in range(mid):
            if ladder[j][tmp][0] == 1:
                if ladder[j][tmp][1] == '-':
                    tmp += 1
                else:
                    tmp -= 1
        up[tmp] = s[i]

    for i in range(k):
        tmp = i
        for j in range(n - 1, mid, -1):
            if ladder[j][tmp][0] == 1:
                if ladder[j][tmp][1] == '-':
                    tmp += 1
                else:
                    tmp -= 1
        down[tmp] = arr[i]

    result = ''
    flag = False
    for i in range(k - 1):
        if len(result) == k - 1:
            break
        if flag:
            flag = False
            continue
        
        if up[i] == down[i + 1] and down[i] == up[i + 1]:
            result += '-*'
            flag = True
        elif up[i] == down[i]:
            result += '*'
        else:
            result = 'x' * (k - 1)
            break
    
    print(result[:-1]) if len(result) > k - 1 else print(result)