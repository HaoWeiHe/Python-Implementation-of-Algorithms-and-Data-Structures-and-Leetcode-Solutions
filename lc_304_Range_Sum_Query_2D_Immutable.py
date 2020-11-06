#21 22 23

# r from 2 to 4
# col from 1 to 3
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if  matrix: 
            m,n = len(matrix), len(matrix[0])

            self.dp = matrix[:]
           
            
            for i in range(m):
                for j in range(1,n):
                    self.dp[i][j] = self.dp[i][j-1] + matrix[i][j]
            self.dp = [[0] + e for e in self.dp]
            
    def sumRegion(self, row1, col1, row2, col2):
        if not self.matrix: 
            return []
        res = 0
        
        for r in range(row1, row2+1):
            res += self.dp[r][col2+1] - self.dp[r][col1]
        
        return res
        
    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)