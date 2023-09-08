from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    total1, total2 = sum(queue1), sum(queue2)
    cnt = 0
    while total1 != total2:
        if cnt == (len(queue1) + len(queue2)) * 2:
            return -1
        if total1 > total2:
            total1 -= queue1[0]
            total2 += queue1[0]
            queue2.append(queue1.popleft())
        else:
            total2 -= queue2[0]
            total1 += queue2[0]
            queue1.append(queue2.popleft())
        cnt += 1
    return cnt
