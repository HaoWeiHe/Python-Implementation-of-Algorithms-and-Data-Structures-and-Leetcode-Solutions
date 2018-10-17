class Solution(object):

	def __init__(self):
		self.res = []

	def helper(self,tmp,count,level,nums,level_count):
		# print("count {} level {} tmp {}".format(count,level_count,tmp))
		for idx in range(len(level)):
			if level_count == len(nums):
				# print(tmp)
				self.res.append(tmp[::])
				# self.res.append(''.join(str(tmp)))
				return 
			if count[idx] == 0:
				continue
			tmp[level_count] = level[idx]
			count[idx] -= 1
			self.helper(tmp,count,level,nums,level_count+1)
			count[idx]  += 1

	def permuteUnique(self, nums):
		dic = dict()
		for num in nums:
			if num in dic:
				dic[num] += 1
			else:
				dic[num] = 1

		count, level = [], []
		for key in dic:
			count.append(dic[key])
			level.append(key)
		# print(count,level)
		self.helper([0 for i in range(len(nums))],count,level,nums,0)
		# print(self.res)
		return self.res
