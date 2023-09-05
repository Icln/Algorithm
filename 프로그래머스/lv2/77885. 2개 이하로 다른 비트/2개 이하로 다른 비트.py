def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            num = '0' + bin(number)[2:]
            num = num[:num.rindex('0')] + '10' + num[num.rindex('0') + 2:]
            answer.append(int(num, 2))

    return answer