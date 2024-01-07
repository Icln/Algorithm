from itertools import combinations
def cal(n, a, b, curA, curB, dice, arrA, arrB):
    if n == len(dice) // 2:
        arrA.append(curA)
        arrB.append(curB)
        return
    for i in range(6):
        cal(n + 1, a, b, curA + dice[a[n]][i], curB + dice[b[n]][i], dice, arrA, arrB)
        
def solution(dice):
    n = len(dice)
    case = set(i for i in range(n))
    result = []
    for a in combinations(case, n // 2):    
        b = tuple(case - set(a))
        arrA, arrB = [], []
        cal(0, a, b, 0, 0, dice, arrA, arrB)
        arrA.sort()
        arrB.sort()
        
        cnt, cur = 0, 0
        for tmp in arrA:
            while cur < len(arrB) and arrB[cur] < tmp:
                cur += 1
            cnt += cur
        result.append([a, cnt])
    
    result.sort(key=lambda x: x[1], reverse = True)
    return [i + 1 for i in result[0][0]]
   