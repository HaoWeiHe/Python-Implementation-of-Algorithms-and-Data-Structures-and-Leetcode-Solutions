class Solution(object):
	def longestPalindrome(self, s):

		dic = dict()
		res = 0 
		for elem in s:
			if elem in dic:
				if dic[elem] ==1:
					res += 1
					
				dic[elem] = dic[elem]%2
				dic[elem] +=1

			else:
				dic[elem] = 1

		res = res*2
		return res + 1 if (res < len(s)) else res
