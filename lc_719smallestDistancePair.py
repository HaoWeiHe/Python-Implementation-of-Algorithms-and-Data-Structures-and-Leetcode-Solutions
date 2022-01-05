
class Solution():
	def smallestDistancePair(self,nums, k):
		
		"""

		"""
		def possible(guess):
			count, left = 0, 0
			for right, x in enumerate(nums):
				while x - nums[left] > guess:
					left += 1
				count += right - left
			return count >= k

	
		nums.sort()
		l, r = 0, nums[-1] - nums[0]
		while l < r:
			mid = l + (r - l ) / 2
			if possible(mid):
				r = mid
			else:
				l = mid + 1
		return l
# nums = [1,3,1]
# k = 1
# print(Solution().smallestDistancePair(nums, k))
