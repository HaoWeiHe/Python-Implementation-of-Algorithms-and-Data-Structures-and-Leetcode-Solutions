class Solution(object):
    def searchMatrix(self, matrix, target):
        """
  
        """
        row, col = len(matrix[0])-1, 0
        while row >= 0 and col < len(matrix):
            if matrix[col][row]  == target:
                return 1
            if matrix[col][row] > target:
                row -=1
            else:
                col +=1
        return 0
        