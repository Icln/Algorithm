def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    s1 = [str1[i] + str1[i + 1] for i in range(len(str1) - 1) 
          if 'A'<= str1[i] <= 'Z' and 'A'<= str1[i + 1] <= 'Z']
    s2 = [str2[i] + str2[i + 1] for i in range(len(str2) - 1) 
          if 'A'<= str2[i] <= 'Z' and 'A'<= str2[i + 1] <= 'Z']
    
    union, intersection = 0, 0
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    elif set(s1) == set(s2) and len(set(s1)) == 1:
        intersection = min(len(s1), len(s2))
        union = max(len(s1), len(s2))
    elif len(s1) != len(set(s1)) or len(s2) != len(set(s2)):
        arr = list(set(s1) & set(s2))
        for i in arr:
            intersection += min(s1.count(i), s2.count(i))   
        
        arr = list(set(s1) | set(s2))
        for i in arr:
            union += max(s1.count(i), s2.count(i))   
    
        print(intersection, union)
    else:
        print(4)
        intersection = len(set(s1) & set(s2))            
        union = len(set(s1) | set(s2)) 
    return int(intersection / union * 65536)
    