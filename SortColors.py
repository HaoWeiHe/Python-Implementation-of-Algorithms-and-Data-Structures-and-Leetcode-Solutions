class Solution(object):
	def sortColors(self, nums):

		res,j,k= list(),0,0

		for i in range(len(nums)):
			v = nums[i]
			nums[i] = 2
			

			if v < 2:
				nums[j] = 1
				j+=1

			if v ==0:
				nums[k] = 0
				k+=1
