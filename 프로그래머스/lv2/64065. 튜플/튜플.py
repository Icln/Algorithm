def solution(s):
    s = s[2: -2].split('},{')
    s.sort(key = lambda x : len(x))
    arr = []
    
    for i in s:
        for j in i.split(','):
            if int(j) not in arr:
                arr.append(int(j))
    
    return arr