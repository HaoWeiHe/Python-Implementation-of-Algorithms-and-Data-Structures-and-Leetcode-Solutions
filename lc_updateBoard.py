class Solution(object):
	def updateBoard(self, board, click):
		"""
		:type board: List[List[str]]
		:type click: List[int]
		:rtype: List[List[str]]
		"""
		#if 8 dir have mine, change and return 
		#if 8 dir no mine, keep going
		x,y = click

		m,n = len(board), len(board[0])
		ds = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
		def dfs(x,y,visted):

			if (x,y) in visted: return 
			
			if 0> x or x >= m or 0 > y or y >= n:return 
			# print(m,n,x,y)
			visted.append((x,y))
			digital = 0
			for dx, dy in ds :
				r, c = dx+x, dy+y
				if 0<=r < m and 0 <=c < n:
					if board[r][c] =="M":  digital+=1

			if digital ==0:
				board[x][y] ="B"
				for dx,dy in ds:
					dfs(x+dx,y+dy,visted)
			else:
				board[x][y] = str(digital)
		if board[x][y] == "M": 
			board[x][y] ="X" 
		else:
			dfs(click[0],click[1],[])
		return board

board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(Solution().updateBoard(board,click))