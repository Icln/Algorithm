n = int(input())

dic = {}
for _ in range (n):
    name, inCompany = input().split()
    if inCompany == 'leave':
        del dic[name]
    else :
        dic[name] = inCompany

dic = sorted(dic.items(), reverse = True)
for i in dict(dic).keys():
    print(i) 