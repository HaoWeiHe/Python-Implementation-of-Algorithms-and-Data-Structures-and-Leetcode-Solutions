class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        
        if not matrix:
            return 0
  
        
        if len(matrix[:]) ==2:
            if ((int(matrix[0][0]) or int(matrix[0][1]) or (matrix[1][0])) =='0') and  matrix[1][1] == '0':
                
                return 0
            else:
                if matrix[1][1] =='1':
                    res = min(int(matrix[0][0]), int(matrix[0][1]), int(matrix[1][0])) + 1
                    return res **2
                else:
                    return 1
         
        if '1' in matrix[0]:
            res = 1
        
        
        for j in range(len(matrix[:])):
            if matrix[j][0]== '1':
                res = 1
                break
                
        for i in range(1, len(matrix[:])):
            
            for j in range(1,len(matrix[0])):
                
                if not matrix[i][j] == '0' :

                    matrix[i][j] = min(int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1])) + 1
                    # print(matrix[i][j],i,j)
                    res = max(res,matrix[i][j] )
                    
        return res**2