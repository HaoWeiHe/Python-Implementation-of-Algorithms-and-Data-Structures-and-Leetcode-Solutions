class Solution(object):
	def maxProduct(self, nums):

		if not nums:
			return 0 
		_max, _min, res = nums[0],nums[0], nums[0]
		
		nums = nums[1:]

		for elem in nums:
			if elem < 0:
				_max, _min = _min, _max
			_max = max(elem, elem*_max)
			_min = min(elem, elem*_min)

			res = max(res, _max)
		return res