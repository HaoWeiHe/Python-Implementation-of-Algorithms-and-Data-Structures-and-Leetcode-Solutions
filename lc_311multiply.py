class Solution(object):
    def multiply(self, A, B):
        """
       [0][0] = A00*B00 + A10*B01+A20*B02
        [0][1] = 
        
        
        [x][y] = [x][:] * [:][y]
        """
 
        m,n = len(A), len(A[0]) #2*3
        m2,n2 = len(B), len(B[0])
        res = [[0]*n2 for _ in range(m)]
        for i in range(len(res)):
            for j in range(len(res[0])):
                for k in range(n):
                    res[i][j]+= A[i][k] * B[k][j]
        return res