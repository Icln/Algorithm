import sys
input = sys.stdin.readline

def change(idx, arr):
    arr[idx], arr[idx + 1], arr[idx + 2] = next[arr[idx]], next[arr[idx + 1]], next[arr[idx + 2]]

def on(arr):
    cnt = 0
    for i in range(1, n - 2):
        while arr[0] != arr[i]:
            change(i, arr)
            cnt += 1

    return cnt if len(set(arr)) == 1 else sys.maxsize

next = {'R':'G', 'G':'B', 'B':'R'}
n = int(input())
s = list(input().rstrip())
answer = sys.maxsize

for i in range(3):
    answer = min(answer, on(s[:]) + i)
    change(0, s)

print(answer if answer != sys.maxsize else -1)