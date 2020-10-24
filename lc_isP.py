
class Solution(object):
	def validPalindrome(self, s):
		for i in xrange(len(s) / 2):
			if s[i] != s[~i]:
				j = len(s) - 1 - i
				temp1 = s[:i] + s[i+1:]
				temp2 = s[:j] + s[j+1:]
				return (temp1 == temp1[::-1]) or (temp2 == temp2[::-1])
		return True

s = "eedcee"
print(Solution().validPalindrome(s))