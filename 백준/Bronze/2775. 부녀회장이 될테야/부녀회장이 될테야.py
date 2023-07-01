t = int(input())

for i in range(t):
    k = int(input())        # 층
    n = int(input())        # 호
    people = [i for i in range(1, n+1)]     # 0층

    for x in range(k):
        new = []
        for y in range(n):
            new.append(sum(people[:y+1]))   # 아래층의 1~n호 까지의 합
        people = new.copy()
        #print(people)		# peaple에 들어있는 값 출력해 봄
    print(people[-1])   