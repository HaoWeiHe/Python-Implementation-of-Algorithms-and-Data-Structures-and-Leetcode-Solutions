class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        from the leftbottom
        less : up
        larger: right
        """
        m,n = len(matrix), len(matrix[0])
        i,j = m-1, 0 
        while i >=0 and j >=0 and i < m and j < n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False