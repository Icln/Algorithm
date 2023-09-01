def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        tmp = ''
        for j in i:
            if j in skill:
                tmp += j
        flag = True 
        for j in tmp:
            if tmp.index(j) != skill.index(j):
                flag = False
                break
        if flag:
            answer +=1
        
    
    return answer