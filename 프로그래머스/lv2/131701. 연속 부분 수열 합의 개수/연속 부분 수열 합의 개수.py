def solution(elements):
    result = set()
    length = len(elements)
    tmp = 0
    for i in range(length - 1):
        for j in range(length):
            if j + tmp > length - 1:
                result.add(sum(elements[j:]) +sum(elements[0 : (j + tmp) - (length - 1)]))
            else:
                result.add(sum(elements[j : j + tmp + 1]))
        tmp += 1             
    return len(result) + 1