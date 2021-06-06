"""
 s= "abc"
 0) ""
 1) a  +  ( "" )
 2) ba, ab, b  + (a, " " )
 3) cab, acb, abc, bc, cb, ac, ca, c

{" "}
{" ", a}
{" ", b, ab, ba}

"""


class Solution():
	def __init__(self):
		self.ans = []

	def helper(self, s):
		"""
		f(abc) = [a + f(bc), b + f(ac) , c + f(ab))
		f(ab) = [a+f(b), b + f(a)]
		f(b) = [s]
		"""
		self.ans += [s]
		if len(s) == 1:
			return [s]
		res = []
		
		for i,v in enumerate(s):
			res.extend([v + ele for ele in self.helper(s[:i] + s[i+1:]) ])
		return res

	def permutations(self,s):
		self.helper(s)
		return self.ans

	def permutations2(self,s):
		sub, ans = [], [" "]
		for i, v in enumerate(s):
			sub = []
			for v2 in ans:
				for idx in range(len(v2)):
					sub.append(v2[:idx] + v + v2[idx:])
			ans.extend(sub)
		ans.remove(" ")
		return ans

print(Solution().permutations('abc'))
