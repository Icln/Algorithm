from itertools import product
def solution(users, emoticons):
    rates = [40, 30, 20, 10]
    answer = []
    for rate in product(rates, repeat = len(emoticons)):
        cnt, price = 0, 0
        for user in users:
            user_rate, user_price = user
            cur_cnt, cur_price = 0, 0

            for i, j in zip(rate, emoticons):
                if i >= user_rate:
                    cur_price += (j // 100 * (100 - i))
                    
                if cur_price >= user_price:
                    cur_cnt += 1
                    break

            if cur_cnt == 1:
                cnt += 1
            else:
                price += cur_price

        answer.append([cnt, price])
    return sorted(answer, key = lambda x: (-x[0], -x[1]))[0]