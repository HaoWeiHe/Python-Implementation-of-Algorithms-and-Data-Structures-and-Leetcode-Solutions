class Solution(object):
    def rotate(self, matrix):
        """
        dia_tran:
        00  01  02 03 
        11  12  13
        22  23
        33
            
                
        left-right(same row)
        for c in range(m)
         for r range(n):
            change(matrix[c][r], matrix[c][m-r])
        """
        n = len(matrix)
        def dia_tran():
            for i in range(n):
                for j in range(i,n):
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        def lf():
            for c in range(n):
                for r in range(n//2):
                    matrix[c][r], matrix[c][n-r-1] = matrix[c][n-r-1], matrix[c][r]
        dia_tran()
        lf()