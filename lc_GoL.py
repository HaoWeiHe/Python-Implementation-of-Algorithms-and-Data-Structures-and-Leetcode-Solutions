0
1
2 live-> die < 2 or live -> die  > 3   
3 die -> live 3 live


class Solution(object):
	def gameOfLife(self, board):

		m,n = len(board),len(board[0])
		
		dirs = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

		for i in range(m):
			for j in range(n):
				live_count = 0
				for x,y in dirs:
					nx, ny = i+x, j+y
					if ni >= m or ni < 0 or nj >= n or nj < 0:
						continue
					if (board[i][j] ==1 or board[i][j] ==2):
						live_count +=1
				if (board[i][j] ==1 or board[i][j] ==2) and (live_count < 2 or live_count >3):
					board[i][j] = 2
				if board[i][j]==0 and live_count==3:
					board[i][j]=3
		return board
 						


board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Solution().gameOfLife(board)