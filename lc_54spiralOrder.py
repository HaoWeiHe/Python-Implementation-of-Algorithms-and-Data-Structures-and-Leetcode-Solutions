import numpy
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []
        while 1:

            res.extend(matrix[0])
            matrix = matrix[1:]
            if len(matrix) == 0:
                break
            matrix = numpy.rot90(matrix)
            
        return res
