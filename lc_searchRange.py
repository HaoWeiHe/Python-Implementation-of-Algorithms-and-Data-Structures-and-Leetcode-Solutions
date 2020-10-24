# nums = [5,7,7,8,8,10], target = 8
# 		0 1 2 3 4 5
# 		mid  =3
# 		[5,7,7][8,8,10]
# 		if target == mid, go for right + left 
# 		if target > mid right
# 		if target < mid left
# mid = 0,5/2 2

class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		self.mn, self.mx = len(nums), -1

		def dfs(i,j):
			if i <=j:
				mid  = (i+j)/2
				if nums[mid] < target:
					dfs(mid +1 , j)
				elif nums[mid] > target:
					dfs(i,mid-1)
				else:
				# print("hey",)
					self.mn = min(self.mn, mid)
					self.mx = max(self.mx, mid)
					dfs(mid+1,j)
					dfs(i,mid-1)
		dfs(0,len(nums)-1)
	   	return [self.mn, self.mx] if self.mn!=len(nums) and self.mn!=-1 else [-1,-1]

nums = [5,7,7,8,8,10]
target = 11
print(Solution().searchRange(nums,target))

