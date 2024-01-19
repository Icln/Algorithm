def solution(price, money, count):
    answer = (count * (1 + count)/2) * price
    if answer < money:
        return 0
    else:
        return int(answer - money)