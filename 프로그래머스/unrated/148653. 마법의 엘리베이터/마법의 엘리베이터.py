def solution(storey): 
    answer = 0
    storey = list(map(int, str(storey)))

    while storey:
        cur = storey.pop()
        if cur == 5:
            if (storey and storey[-1] < 5) or not storey:
                answer += cur
            else:
                answer += (10 - cur)
                storey.append(storey.pop() + 1)
        else:
            if cur < 5:
                answer += cur
            else:
                answer += (10 - cur)
                if storey:
                    storey.append(storey.pop() + 1)
                else:
                    answer += 1

    return answer
