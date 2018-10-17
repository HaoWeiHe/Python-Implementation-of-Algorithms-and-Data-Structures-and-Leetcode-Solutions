class Solution(object):
	def longestValidParentheses(self, s):
		if not s :
			return 0
		dp = [0 for i in range(len(s))]

		for idx in range(1,len(s)):
			if s[idx] == ")":
				j = idx-1-dp[idx-1]

				if j >=0 and s[j] =="(":
					dp[idx] = dp[idx-1]+2
					if j >=1:
						dp[idx]+=dp[j-1]
		return max(dp)