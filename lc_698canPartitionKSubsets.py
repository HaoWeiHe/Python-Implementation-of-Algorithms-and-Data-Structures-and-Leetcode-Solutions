class Solution(object):
	def canPartitionKSubsets(self, nums, k):
		"""
		[4,3,2,3,5,2,1],
		
		k = 4,
		s = sum of subsets
		total = 4s = sum([4,3,2,3,5,2,1])
		so, s = sum([3,4.2,3,5,2,1])/k = 5
		3: get 2 in [4,2,3,5,2,1]
			 if 2 ,finish
			 if 1: get 1 in [4,2,3,5,2]
		"""
		target = sum(nums)/k

		d = [False]* len(nums)

		self.ans = False

		def dfs(d, ret, counter):

			if counter == k:
				self.ans = True
				return 

			if ret == 0:
				dfs(d, target, counter +1)
				return

			for idx, v in enumerate(d):
				val = nums[idx]
				if v or val > ret:
					continue
				d[idx] = True
				dfs(d, ret - val, counter)
				d[idx] = False
			
		
		dfs(d, target,0) 
		return self.ans

nums, k =[1,2,3,4], 3
print(Solution().canPartitionKSubsets(nums, k))