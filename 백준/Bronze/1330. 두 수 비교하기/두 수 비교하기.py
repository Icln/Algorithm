A,B = map(int,input().split())
if A > B:
    print('>')  # if 조건식이 참일 때 문장
elif A < B:
    print('<')  # if조건식이 참이 아닌경우 elif 조건식이 참일 때 문장
else:
    print('==') 