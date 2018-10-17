
class Solution(object):
	def searchRange(self, nums,target):
		start, end = -1,-1
		for idx in range(len(nums)):
			if target == nums[idx]:
				if start == -1:
					start = idx
					end = idx
				else:
					end = idx
		return [start, end]