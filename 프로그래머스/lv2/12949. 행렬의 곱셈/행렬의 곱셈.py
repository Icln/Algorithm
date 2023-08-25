def solution(arr1, arr2):
    l1, l, l2 = len(arr1), len(arr2), len(arr2[0])
    answer = []
    
    for i in range(l1):
        tmp = []
        for k in range(l2):
            mul = 0
            for j in range(l):
                mul += arr1[i][j] * arr2[j][k]
            tmp.append(mul)
        answer.append(tmp)
    return answer