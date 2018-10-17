
class Solution(object):



	def threeSum(self, lst):
		
		tmp = []
		tmp_res = [[]]
		res = []
	
		for elem in lst:
			for r in tmp_res:
				tmp.extend([r+[elem]])
	
			
			tmp_res.extend(tmp)
			tmp = []

		for elem in tmp_res:
			if len(elem)== 3:
				if (sum(elem) ==0):
					res.append(sorted(elem))
				
		ress = [list(item) for item in set(tuple(row) for row in res)]
		return ress
