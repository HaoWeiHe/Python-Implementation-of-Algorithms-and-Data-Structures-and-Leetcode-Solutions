# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        from the left  right to bottom left 
        [      1   ]
        [   1 0    ]
        """
        m, n = binaryMatrix.dimensions() 
        i,j = -1,-1
        upperbound = n
        for row in range(m):
            for pivot in range(upperbound-1,-1,-1):
                if  binaryMatrix.get(row,pivot) == 1:
                    upperbound = pivot
                else: break
        return upperbound if upperbound != n else -1
                
        
        
    def leftMostColumnWithOne2(self, binaryMatrix):
        """
        bfs for every rows and append it to res
     
        """
        res = []
        
        m, n = binaryMatrix.dimensions() 
        
        def bfs(i):
            l,r = 0,n #l is the smallest 1  [1,r )
           
            while l < r:
                mid = l + (r -l )/2
                if binaryMatrix.get(i,mid) == 0:
                    l = mid +1
                else:
                    r = mid 
            
            return l 


        for c in range(m):
            res.append(bfs(c))
        m_v = min(res)
        return m_v if m_v!= n else -1 