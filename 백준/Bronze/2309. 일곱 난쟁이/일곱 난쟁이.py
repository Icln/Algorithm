import itertools

array = [int(input()) for _ in range(9)]

for i in itertools.combinations(array, 7):  # 해당 배열을 7명 중복없이 뽑아준다.
    if sum(i) == 100:  # 그합이 100이라면
        for j in sorted(i):  # 그 7명을 오름차순으로 정렬후 출력한다.
            print(j)
        break #그 후 반복문 탈출