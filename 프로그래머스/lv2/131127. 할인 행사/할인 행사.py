def solution(want, number, discount):
    l = len(discount)
    buy = dict()
    for i in range(len(want)):
        buy[want[i]] = number[i]
    
    answer = 0
    for i in range(l - 9):
        tmp = discount[i : i + 10]
        flag = True
        for j in buy:
            if buy[j] != tmp.count(j):
                flag = False
                break
        if flag:
            answer += 1
    return answer