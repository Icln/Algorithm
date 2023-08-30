arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def solution(n, t, m, p):
    answer = ''
    target = 0
    s = ''
    while t > 0:
        s += jinsu(n, target)
        if len(s) > p:
            answer += s[p - 1]
            t -= 1
            p += m

        target += 1  
    return answer

def jinsu(n, num):
    tmp = ''
    while num > n - 1:
        tmp += arr[num % n]
        num //= n
    return ''.join(reversed(tmp + str(arr[num])))