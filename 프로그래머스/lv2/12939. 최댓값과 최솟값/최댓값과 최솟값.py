def solution(s):
    num = [int(i) for i in s.split()]
    answer = ''
    answer = str(min(num)) + ' ' + str(max(num))
    return answer