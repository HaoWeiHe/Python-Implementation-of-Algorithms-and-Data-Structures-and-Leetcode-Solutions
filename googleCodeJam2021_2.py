import collections
T = int(raw_input())
# T = 1
for number in range(T):
	can = []
	n = raw_input()
	lst = map(int,raw_input().split(" "))

	s = lst
	ans = "A"
	
	for idx, e in enumerate(s):
		idx += 1
		if idx %2 == 1 :#even
			for i in range(66, 66 + e-1):
				ans += chr(i)
			if idx != len(s) and e < s[idx]:
				#change the last one
				ans += chr(65 + s[idx])
			else:
				ans += chr(65 + e)
				
		else:
			for i in range(65 + e-1, 64, -1):
				ans += chr(i)
	print("Case #{}: {}".format(number + 1, ans))