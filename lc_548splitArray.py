

class Solution(object):
	def splitArray(self, nums):
		"""
	
		"""
		pre = 0
		acc = []
		for ele in nums:
			acc.append(pre + ele)
			pre = ele+ pre
		n = len(nums)
		
		for j in range(2,n-3):
			record = set()
			for i in range(j-1):
				sum1 = acc[i-1]
				sum2 = acc[j-1] - acc[i]
				if sum1 == sum2:
					record.add(sum1)
			for k in range(j+1, n-1):
				sum1 = acc[k-1] - acc[j]
				sum2 = acc[n-1] - acc[k]
				if sum1 == sum2 and sum1 in record:
					return True
		return False
