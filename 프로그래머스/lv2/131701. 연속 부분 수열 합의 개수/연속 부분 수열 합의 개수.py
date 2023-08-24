def solution(elements):
    result = set()
    length = len(elements)

    for i in range(length):
        sum = elements[i]
        result.add(sum)
        for j in range(i + 1, i + length):
            sum += elements[j % length]
            result.add(sum)
    return len(result)