import math
def solution(n, k):
    nString = jinsu(n,k)
    answer = 0
    
    for i in nString.split('0'):
        if i.isdigit():
            print(int(i))
            if check(int(i)):
                answer += 1
    
    return answer

def jinsu(n, k):
    if n == 10:
        return str(n)
    tmp = ''
    while n >= k:
        tmp += str(n % k)
        n //= k
    return ''.join(reversed(tmp + str(n % k)))
    
def check(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0 and n // i != 1:
            return False
    return True