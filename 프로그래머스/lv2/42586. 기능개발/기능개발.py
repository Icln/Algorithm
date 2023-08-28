from math import ceil
def solution(progresses, speeds):
    s = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    idx = 0
    arr = []
    for i in range(len(s)):
        if s[idx] < s[i]:
            arr.append(i - idx)
            idx = i
             
    return arr + [len(s) - idx]
