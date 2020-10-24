
class Solution(object):
	def numEnclaves(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		m,n = len(A),len(A[0])
		
		def dfs(x,y):
			
			if A[x][y]==0: return 
			A[x][y] = 0
			dirs = [[0,1],[1,0],[0,-1],[-1,0]]
			for dx,dy in dirs:
				newx, newy = x+dx, y + dy
				if 0<= newx < m and 0 <= newy <n:
					if A[newx][newy] ==1: 
						dfs(newx,newy)

		for i in range(m):
			if A[i][0] ==1: dfs(i,0)
			if A[i][n-1]==1: dfs(i,n-1)
		for j in range(n):
			if A[0][j] ==1: dfs(0,j)
			if A[m-1][j]==1: dfs(m-1,j)
		# return all()
		return sum([sum(a) for a in A])

A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
#00, 01 02 10 20 30 m0 m1 m2 
print(Solution().numEnclaves(A))
