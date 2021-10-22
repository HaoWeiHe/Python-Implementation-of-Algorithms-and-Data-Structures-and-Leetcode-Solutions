class Solution(object):
	def solveNQueens(self, n):
		"""
		[[".Q..",
		  "...Q",
		  "Q...",
		  "..Q."]
		  
		 ["Q..."]
		 ["..Q."]
		 [1,3,] X
		 ---------------
		 
		 [".Q.."]
		 ["...Q"]
		 [2,4,1,3]
		 
		 ["..Q."]
		 [3,1,4,2]
		 
		 ["...Q"]
		 [4,1]
			[4,1] -> no where to put X
		 [4,2] ->
		  """
		self.ans = []
		def dfs(lst, dia1, dia2):
			if len(lst) == n:
				tmp = []
				for ele in lst:
					s = ["." for i in range(n)]
					s[ele] = "Q"
					tmp.append("".join(s))
				self.ans.append(tmp)
				return 

			for i in range(n):
				# if not lst:
				# 	dfs(lst+[i],[],[])
				# 	continue
				dia1_code = len(lst) + i #x + y 
				dia2_code = len(lst) - i + n -1 #x - y + n -1
				if i in lst or dia1_code in dia1 or dia2_code in dia2:
					continue

				dfs(lst+[i], dia1 + [dia1_code], dia2 + [dia2_code])
		dfs([],[],[])
		return self.ans
			
			
print(Solution().solveNQueens(5))