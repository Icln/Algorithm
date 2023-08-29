def solution(str1, str2):
    s1 = [str1[i: i + 2].upper() for i in range(len(str1) - 1) if str1[i: i + 2].isalpha()]
    s2 = [str2[i: i + 2].upper() for i in range(len(str2) - 1) if str2[i: i + 2].isalpha()]
    
    union, intersection = 0, 0
    unionArr = list(set(s1) | set(s2))
    interArr = list(set(s1) & set(s2))
    if len(unionArr) == 0:
        return 65536
    elif len(interArr) == 1:
        intersection = min(len(s1), len(s2))
        union = max(len(s1), len(s2))
    elif len(s1) != len(set(s1)) or len(s2) != len(set(s2)):
        for i in interArr:
            intersection += min(s1.count(i), s2.count(i))   
        for i in unionArr:
            union += max(s1.count(i), s2.count(i))     
    else:
        intersection = len(interArr)            
        union = len(unionArr) 
    return int(intersection / union * 65536)
    