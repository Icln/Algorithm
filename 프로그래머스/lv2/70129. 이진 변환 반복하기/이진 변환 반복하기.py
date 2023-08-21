def solution(s):
    times = 0
    num = 0

    while s != "1":
        num += s.count('0')
        s = s.replace('0','') 
        s = bin(int(len(s)))[2:]
        times += 1

    return [times, num]
