import sys
input = sys.stdin.readline
def hanoi(n, src, dst):
    if n == 1:
        print(src, dst)
        return
    hanoi(n-1, src, 6 - src - dst) # n-1개의 원판을 목표 기둥이 아닌 곳에 배치
    print(src, dst) # 가장 큰 원판을 목표 기둥으로 배치
    hanoi(n-1, 6 - src - dst, dst) # n-1개의 원판을 목표 기둥으로 배치

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)