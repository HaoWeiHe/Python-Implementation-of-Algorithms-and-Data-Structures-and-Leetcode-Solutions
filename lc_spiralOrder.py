import numpy as np
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) ==1:
            return matrix[0]
        
        
        res = []
        while( len(matrix) > 0 ):
            for i in matrix[0]:
                res.append(int(i))
            
            matrix = matrix[1:]
            matrix = np.rot90(matrix)
            
        
        
        return res