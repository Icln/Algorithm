import sys
input = sys.stdin.readline

def Fibo(x):
    if x == 0 :
        return 0
    elif x == 1:
        return 1
    else:
        return Fibo(x - 1) + Fibo(x - 2)

print(Fibo(int(input())))