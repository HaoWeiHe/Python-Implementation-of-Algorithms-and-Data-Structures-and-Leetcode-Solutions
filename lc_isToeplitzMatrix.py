class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix: return 0
        m,n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                nx, ny = i,j
                while True:
                    start = matrix[i][j]
                    nx, ny = nx +1 , ny + 1
                    if nx >= m or ny >= n : 
                        break
                    if start != matrix[nx][ny]:
                        return False
        return True

# 0,0  0,1  0,2   0,3  
# 1,1  1,2  1,3   0,4 
# 2,2  2,3  1,4 > 3, break

# 1,0 2,0
# 2,1 3 > 2,1 break

# i,j : i from 0 to 2(m), j from 0 to 3(n)
# 1+1
# m, n = len()
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

matrix = [
  [1,2],
  [2,2]
]
Solution = Solution().isToeplitzMatrix(matrix)
print(Solution)