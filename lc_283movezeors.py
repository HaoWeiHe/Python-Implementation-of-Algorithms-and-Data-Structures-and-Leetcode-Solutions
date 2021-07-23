class Solution(object):
    def moveZeroes(self, A):
        """
        [0,1,0,3,12]
         i
           j -> every time A[i] ==0, find j and i ++ 
         1 0 0 3 12
           i
               j
        1 3 0 0 12
            i
        1 3 0 0 12
                j
        1 3 12 0 0
               i    
        """
        i, j = 0,0 
        
        while j < len(A) and i < len(A):
            if A[i] == 0:
                j = i + 1
                while j < len(A) and A[j] == 0:
                    j += 1
                if j < len(A):
                    A[i], A[j] = A[j], A[i]
                
            i +=1    
        return A