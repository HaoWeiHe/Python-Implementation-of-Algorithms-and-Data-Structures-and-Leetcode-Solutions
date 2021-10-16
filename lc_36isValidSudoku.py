class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		self.ans = False
		m, n = len(board),len(board[0])
		
		rows = [set() for _ in range(9) ]
		cols = [set() for _ in range(9) ]
		blk = [set() for _ in range(9) ]

		for i in range(m):
			for j in range(n):
				val = board[i][j]

				if val == ".":			
					continue

				val = int(val)
				if val in rows[i]:
					return False
				rows[i].add(val)

				if val in cols[j]:
					return False
				cols[j].add(val)
				
				blk_num = (i/3)*3 + (j/3)
				if val in blk[blk_num]:
					return False
				blk[blk_num].add(val)
		return True
	   			
		
		return self.ans

board =  [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))