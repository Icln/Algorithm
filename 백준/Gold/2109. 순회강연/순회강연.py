import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    days = [0] * 10001
    arr = [list(map(int, input().split())) for _ in range(n)]   
    arr.sort(key=lambda x: -x[0])
    
    for i in range(n):
        p, d = arr[i][0], arr[i][1]
        for j in range(d, 0, -1):
            if days[j] == 0:
                days[j] = p
                break
    print(sum(days))