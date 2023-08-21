def solution(s):
    num = [int(i) for i in s.split()]
    return str(min(num)) + ' ' + str(max(num))