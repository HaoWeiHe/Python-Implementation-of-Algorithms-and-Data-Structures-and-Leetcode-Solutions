class Solution(object):
    def uniquePaths(self, m, n):
        """
     
        1,1,1,1,1,1,1
        1 2 3 4 5 6 7
        1 3 6 10152128
        
        
        1,1,1,1,1,1,1
        1 2 3 4 5 6 7
        1 3 6 10152128
        """
        if m == 0 or n ==0:
            return 0
        lst = [1]* n
        
        for _ in range(m-1):
            for j in range(1,n):
                lst[j] += lst[j-1] 
        return lst[-1]
            