def solution(record):
    arr = dict()
    answer = []
    
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            answer.append([i[1], "님이 들어왔습니다."])
            arr[i[1]] = i[2]
        elif i[0] == "Leave":
            answer.append([i[1], "님이 나갔습니다."])
        else:
            arr[i[1]] = i[2]
    
    answer = list(map(lambda x : arr[x[0]] + x[1], answer))
    return answer
    