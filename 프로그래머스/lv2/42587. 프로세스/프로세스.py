from collections import deque
def solution(priorities, location):
    sortedP = [i for i in priorities]
    sortedP.sort(reverse = True)
    priorities = deque([[i[0], i[1]] for i in enumerate(priorities)])
    idx = 0
    i = 0
    while True:
        if sortedP[idx] != priorities[i][1]:
            priorities.append(priorities.popleft())
        else:
            if priorities[i][0] == location:
                return i + 1
            idx += 1
            i += 1
            continue
    
    