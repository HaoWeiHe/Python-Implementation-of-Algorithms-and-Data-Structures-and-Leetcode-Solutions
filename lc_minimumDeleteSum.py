class Solution(object):
	def minimumDeleteSum(self, w1, w2):
		"""
		:type s1: str
		:type s2: str
		:rtype: int
		"""

		if not w1 and not w2: return 0
		if not w1 : return len(w2)
		if not w2 : return len(w1)
		# sea, eat
		m, n = len(w2), len(w1)

		dp = [ [0]*(n+1) for _ in range(m+1) ]
		print(dp)
		for  i in range(1, m+1):
			dp[i][0] = dp[i-1][0] + ord(w2[i-1])
		
		for j in range(1, n+1):
			dp[0][j] = dp[0][j-1] + ord(w1[j-1])

		
		for i in range(1, m+1):
				for j in range(1, n+1):
					a, b = ord(w2[i-1]), ord(w1[j-1])
					if w2[i - 1] == w1[j - 1]:
						dp[ i ][ j ] = dp[ i -1 ][ j -1 ]
					else:
						dp[ i ][ j ] = min(dp[ i -1 ][ j -1 ] + a + b, dp[ i -1 ][ j  ] +a, dp[ i ][ j -1 ] +b)

		return dp[-1][-1]

s1,s2 = "sezza", "eat"
print(Solution().minimumDeleteSum(s1,s2))