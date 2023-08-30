alpha =['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def solution(msg):
    answer = []
    idx = 0
    while True:
        tmp = ''
        l = idx
        while True:
            if l < len(msg):
                tmp += msg[l]
                if tmp in alpha:
                    l += 1
                    continue 
            if tmp in alpha:    
                answer.append(alpha.index(tmp))
            else:
                answer.append(alpha.index(tmp[:-1]))
            alpha.append(tmp)    
            break
        
        if l == len(msg):
            break        
        idx += len(tmp) - 1 
    return answer