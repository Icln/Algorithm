import math
def solution(s):
    result = []
    for i in range(len(s) // 2, 0, -1):
        tmp = s[:i]
        cnt = 1
        st = ''
        for j in range(1, math.ceil(len(s) / i) + 1):
            if tmp != s[i * j : i * (j + 1)]:
                if cnt != 1:
                    st += (str(cnt) + tmp)
                else:
                    st += tmp
                tmp = s[i * j : i * (j + 1)]
                cnt = 1
            else:
                cnt += 1
        result.append(st)
    
    return len(min(result, key = len)) if len(result) != 0 else 1