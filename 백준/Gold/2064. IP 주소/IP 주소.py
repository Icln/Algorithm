import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        a, b, c, d = map(int, input().split('.'))
        num = bin(a) + bin(b)[2:] + bin(c)[2:] + bin(d)[2:]
        arr.append(format(a, '08b') + format(b, '08b') + format(c, '08b') + format(d, '08b'))

    cnt = 32
    for i in range(1, n):
        for j in range(32):
            if arr[0][j] != arr[i][j]:
                cnt = min(cnt, j)
                break

    mask = '1' * cnt + '0' * (32 - cnt)
    print(f'{int(mask[:8], 2) & int(arr[0][:8], 2)}.{int(mask[8:16], 2) & int(arr[0][8:16], 2)}.{int(mask[16:24], 2) & int(arr[0][16:24], 2)}.{int(mask[24:32], 2) & int(arr[0][24:32], 2)}')
    print(f'{int(mask[:8], 2)}.{int(mask[8:16], 2)}.{int(mask[16:24], 2)}.{int(mask[24:32], 2)}')
