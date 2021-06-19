class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        simulation to flat the 2 d arrary into 1d and use binary search approach
        len(col) = n
        l, r = 0 , m*n
        row, col = value/n, value% n 
        
        """
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0]) 
        l, r = 0, m*n
        
        while l < r:
            mid = l + (r-l)/2
            
            row, col = mid / n, mid % n
            
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                r = mid
            else:
                l = mid + 1
        return False
        
    def searchMatrix2(self, matrix, target):
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