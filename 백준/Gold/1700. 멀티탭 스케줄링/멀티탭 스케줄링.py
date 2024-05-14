import sys
input = sys.stdin.readline

def find_latest(idx):
    result = 0
    max_idx = -1
    for num in plug:
        try:
            num_idx = arr[idx:].index(num)
        except:
            num_idx = k
            
        if max_idx < num_idx:
            result, max_idx = num, num_idx

    return result

if __name__ == "__main__":
    n, k = map(int, input().split())
    if n >= k:
        print(0)
        exit()

    arr = list(map(int, input().split()))
    plug = set()
    cnt = 0

    for idx, num in enumerate(arr):
        plug.add(num)
        if len(plug) > n:
            cnt += 1
            tmp = find_latest(idx)
            plug.discard(tmp)

    print(cnt)