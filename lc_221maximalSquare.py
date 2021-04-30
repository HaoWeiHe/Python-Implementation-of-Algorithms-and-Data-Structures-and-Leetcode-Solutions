class Solution(object):
    def maximalSquare(self, matrix):
        """
        if dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i][j-1]) + 1 if dp[i][j] == 1 
        append
        """
        if not matrix:return 0

        matrix = [[0]* len(matrix[0])] + matrix

        matrix = [[0] + map(int,e) for e in matrix]
        # num_row, num_col = len(matrix[0]),len(matrix)
        m,n = len(matrix), len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]:
                    up = matrix[i-1][j]
                    left = matrix[i][j-1]
                    dig  = matrix[i-1][j-1]
                    matrix[i][j] = min(up, left, dig) + 1

        return max([max(map( int,e)) for e in matrix ])**2
        