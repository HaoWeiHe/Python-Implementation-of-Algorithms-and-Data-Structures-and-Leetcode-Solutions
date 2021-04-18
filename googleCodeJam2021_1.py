import collections
T = int(raw_input())

for number in range(T):
	can = []
	n = raw_input()
	lst = map(int,raw_input().split(" "))
	
	nl = []
	for e in lst:
		if e!="":
			nl.append(e)
	lst = nl
	c = collections.Counter(lst) #10: 2
	a = sorted(c.items(), key = lambda x: x[0]) 
	ans = 0
	for idx,e in enumerate(a):
		ans += e[1] * (idx+1)
	
	print("Case #{}: {}".format(number + 1, ans))