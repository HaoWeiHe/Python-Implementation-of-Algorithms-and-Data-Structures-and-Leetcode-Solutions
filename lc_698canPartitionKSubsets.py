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
		if target * k != sum(nums):
			return False
		d = [False]* len(nums)

		self.mem = {}

		def dfs(lst, ret, counter):
			if tuple(lst) in self.mem:
				return self.mem[tuple(lst)]

			if counter == k:
				return True

			if ret < 0:
				return False
			
			if ret == 0:
				return dfs(lst, target, counter +1)
			
			for idx in range(len(nums)):
				if lst[idx]:
					continue

				lst[idx] = True

				if dfs(lst, ret - nums[idx], counter):
					self.mem[tuple(lst)] = True
					return True

				lst[idx] = False

			self.mem[tuple(lst)] = False
			return self.mem[tuple(lst)]
			
		return dfs(d, target, 0) 
		

nums, k = [1,2,3,5],2
print(Solution().canPartitionKSubsets(nums, k))
