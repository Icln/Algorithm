def solution(msg):
    answer = []
    alpha = [''] + [chr(ord('A') + i) for i in range(26)]
    idx = 0

    while idx < len(msg):
        tmp = ''
        while idx < len(msg):
            tmp += msg[idx]
            if tmp not in alpha:
                break
            idx += 1
        
        if tmp in alpha:    
            answer.append(alpha.index(tmp))
        else:
            answer.append(alpha.index(tmp[:-1]))    
        alpha.append(tmp)
    
    return answer
