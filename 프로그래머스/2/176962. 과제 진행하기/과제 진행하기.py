def convert(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(plans):
    plans = [[p[0], convert(p[1]), int(p[2])] for p in plans]
    plans.sort(key = lambda x : x[1])

    answer, stack = [], []
    time, idx = plans[0][1], 0
    
    while idx < len(plans):
        stack.append(plans[idx])
        if time < stack[-1][1]:
            time = stack[-1][1]

        while stack and stack[-1][2]:
            time += 1
            stack[-1][2] -= 1
            if not stack[-1][2]:
                answer.append(stack.pop()[0])
            
            if idx + 1 < len(plans) and time == plans[idx + 1][1]:
                stack.append(plans[idx + 1])
                idx += 1
        idx += 1

    return answer


        