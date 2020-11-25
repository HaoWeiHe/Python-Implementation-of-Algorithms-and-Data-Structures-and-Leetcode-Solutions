class Solution:
	def findKthPositive(self, arr, k):
		"""
		[2,3,4,7,11], k = 1
		we lost at least k numbes at T[:l]
		-> 
		m = 2 arr[m] = 4, space = 4 - 3(idx+1) = 1
		lf have 2 space, 2 < k searching rt part. l = 3
		m = 3 arr[m] = 7, space = 7 - 4(idx+1) = 3, l = 4
		m = 4, arr[m] = 11, space = 11 - 5 = 6 > k, r = 4
		"""
		l,r = 0,len(arr)

		while l < r:
			m = (l + r) / 2
			space = arr[m] - (m+1)
			if space >= k:
				r = m
			else:
				l = m +1
		return l + k  
