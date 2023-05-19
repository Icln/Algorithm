word = input().lower()
wl = list(set(word))
cnt =[]
for i in wl:
    cnt.append(word.count(i))
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(wl[(cnt.index(max(cnt)))].upper())