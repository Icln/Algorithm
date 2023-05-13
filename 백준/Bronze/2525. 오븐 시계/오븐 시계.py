A, B = map(int, input().split())
C = int(input())
if B+C >= 60 :
    X  = (B + C) // 60
    if (A + X >= 24) :
        A -= 24
    A += X   
    B +=  C - (60 * X)
else :
    B = B + C
print(f'{A} {B}')    