class Solution(object):
	def maxSumOfThreeSubarrays(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		length = len(nums)
		n = length - k +1 #[1,2,3] #lght = 3, n = 2
		lf = [0 for _ in range(n)]
		rt = [0 for _ in range(n)]
		
		dp = [0 for _ in range(n)]
		s = 0
		
		s = 0
		for i in range(length):
			s += nums[i]
			if i >=k:
				s -=nums[i-k]
			if i >= k-1: 
				dp[i-k+1] = s
		
		
		
		mx_idx = 0
		for i in range(n):
			if dp[i] > dp[mx_idx]: 
				mx_idx = i
			lf[i] = mx_idx

		mx_idx = n-1
		for i in range(n-1,-1,-1): #dp[6]
			if dp[i] >= dp[mx_idx]:
				mx_idx = i
			rt[i] = mx_idx
		res = []
		
		mx = 0
		for i in range(k,n-k):
			cur_val = dp[lf[i-k]] + dp[i] + dp[rt[i+k]]
			if cur_val > mx: 
				res = [ lf[i-k], i, rt[i+k]]
				mx = cur_val
				# print(cur_val,i)
		return res