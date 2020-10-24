class Solution(object):
	def solveNQueens(self, N):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		Quees_ocuuption = {}
		for i in range(N):
			Quees_ocuuption[i] = -1
		dia_occupation = []
		
		res = []
		record = []
		def dfs(QueenNumber):
		
			if QueenNumber == N:

				res.append(record[:])
				return
# Quees_ocuuption {first:2, second: 4}
			for i in range(N):
				dia_occupation = []
				for k,v in Quees_ocuuption.items():
					if v == -1 : continue
					if 0 <=  v  + QueenNumber - k < N   :dia_occupation.append(v  + QueenNumber - k )
					if 0 <= v - (QueenNumber-k)  < N : dia_occupation.append(v - (QueenNumber-k))
				
				if i not in dia_occupation and i not in Quees_ocuuption.values():
					tmp = ["."] *N
					tmp[i] = "Q"
					# print("tmp", tmp)
					record.append("".join(tmp))
				
					
					Quees_ocuuption[QueenNumber] = i
					dfs(QueenNumber + 1) #["Q.",]
					Quees_ocuuption[QueenNumber] = -1
					record.pop()
		dfs(0)

		return res

res = Solution().solveNQueens(4)
print(res)
# for e in res: 
# 	print("====")
# 	for a in e:
# 		print(e)
# 	print("====")
#		 [Q,...,]
#		 [.Q]
		