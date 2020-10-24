class Solution(object):
	def addOperators(self, num, target):
		"""
		:type num: str
		:type target: int
		:rtype: List[str]
		"""
		def dfs(idx =0,record = '', value = 0, pre = None):
			
			if idx == len(num) and value == target: 
				res.append(record)
				return 
			
# [1+2+3]
			for i in range(idx+1, len(num)+1):#1,3
				tmp = int(num[idx:i])
				if i == idx+1 or (i > idx+1 and num[idx]!='0'): #100+1
					if pre == None:

						dfs(i, num[idx:i], tmp, tmp)
					else:
						dfs(i, record + "+" + num[idx:i], value+ tmp, tmp)
						dfs(i, record + "-" + num[idx:i], value - tmp, -tmp)
						dfs(i, record + "*" + num[idx:i], value - pre + tmp*pre, tmp*pre)



		res = []
		dfs()
		return res

num, target = "123",6
Solution().addOperators(num,target)