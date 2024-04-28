import sys

n, w, l = map(int, input().split())
q = list(map(int, input().split()))
 
b = [0] * w
time = 0
while b: 
	time += 1
	b.pop(0) 
	if q: 
		if sum(b) + q[0] <= l:
			b.append(q.pop(0))
		else:
			b.append(0) 
print(time)