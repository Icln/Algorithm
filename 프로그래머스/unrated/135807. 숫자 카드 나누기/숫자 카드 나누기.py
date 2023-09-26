from math import gcd
def solution(arrayA,arrayB):   
    a, b = 0,0
    l = len(arrayA)
    for i in range(l):
        a = gcd(a, arrayA[i])
        b = gcd(b, arrayB[i])

    for i in range(l):
        if arrayA[i] % b == 0:
            b = 1
        if arrayB[i] % a == 0:
            a = 1

    return 0 if a == 1 and b ==1 else max(a, b)


