class NumMatrix(object):

    def __init__(self, matrix):
        """
         [[3, 0, 1], 
         [5, 6, 3]]
         
         [ 3, 3,4]
         [8, 14, ]
        """
        m,n  = len(matrix), len(matrix[0])
        
        for j in range(1,n):
            matrix[0][j] += matrix[0][j-1]
        
        for i in range(1,m):
            
            matrix[i][0] += matrix[i-1][0]

            
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1]
        self.m  = matrix
       
     
    def sumRegion(self, r1, c1, r2, c2):
        """
        r1, c1    r2,c1
        []
        r1,c2        r2,c2
        """ 
        A = self.m[r2][c2] 
        B = self.m[r2][c1-1] if c1!=0 else 0 
        C = self.m[r1-1][c2] if r1!=0 else 0 
        D  = self.m[r1-1][c1-1] if r1!=0 and c1!=0 else 0 

        return  A -B -C +D

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)