class Solution(object):
    def sortedSquares(self, A):
        """
       [-3, -2, -1, 4, 5, 6]
                 i.  j 
             i       j
        i            j
       [1,2,3]
        
        """
        i,j = 0,0
        for idx,v in enumerate(A):
            if v >=0:
                j = idx
                break
        i = j-1
        res = []
        while i >=0 and j < len(A):
            if abs(A[i]) < abs(A[j]):
                res.append(A[i]**2)
                i -=1
            else:
                res.append(A[j]**2)
                j +=1
        
        while i >=0:
            res.append(A[i]**2)
            i -=1
        while j < len(A):
            res.append(A[j]**2)
            j +=1
        return res    
        
        #Solution 1 : sort 
        #A.sort(key = lambda x: abs(x))
        # return [ele**2 for ele in A]
