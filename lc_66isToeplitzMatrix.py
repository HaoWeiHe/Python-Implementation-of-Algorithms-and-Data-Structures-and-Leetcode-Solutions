class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        i, j, m,n = 0, 0, len(matrix), len(matrix[0])
        def check(i,j,target):
            while i < m and j < n:
                if target != matrix[i][j]:
                    return False

                i += 1
                j += 1
            return True
        for cur in range(n):
            i = 0
            j = cur
            target = matrix[i][j] 
            if not check(i,j, target):
                return False
        for cur in range(m):
            i = cur
            j = 0
            target = matrix[i][j]
            if not check(i,j,target):
                return False
        return True