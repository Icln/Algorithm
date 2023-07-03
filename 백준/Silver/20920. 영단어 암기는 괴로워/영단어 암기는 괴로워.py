import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) 
word_list = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) < m: 
        continue
    else: 
        if word in word_list: 
            word_list[word] += 1
        else: 
            word_list[word] = 1

word_list = sorted(word_list.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) 
# x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치 내림차순
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in word_list:
    print(i[0])