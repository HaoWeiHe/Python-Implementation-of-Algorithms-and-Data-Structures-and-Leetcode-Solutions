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
		def dfs(lst):
			if len(lst) == n:
				tmp = []
				for ele in lst:
					s = ["." for i in range(n)]
					s[ele] = "Q"
					tmp.append("".join(s))
				self.ans.append(tmp)
				return 

			for i in range(n):
				flag = True
				if not lst:
					dfs(lst+[i])
					continue
		
				for lvl, idx in enumerate(lst): #[.Q..] if lvl == 2, i - val!= 2
					if i == idx or i == idx + (len(lst) - lvl) or i == idx - (len(lst) - lvl):#idx + lvl == i or idx - lvl == i:
						flag = False
				if flag:
					dfs(lst+[i])
		dfs([])
		return self.ans
			
			
print(Solution().solveNQueens(5))