class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
      
        """
        def dfs(A,B):
            lst = [p1, p2, p3, p4]
            pairs = []
            for e in lst:
                if e!= A and e!=B:
                    pairs.append(e)
            if len(pairs)!=2:return False
            C, D = pairs
           
            return ((B[0] - A[0])**2 +  (B[1] - A[1])**2 ) ==  ((C[0] - D[0])**2 +  (C[1] - D[1])**2 ) != 0  and \
                   ((A[0] - C[0])**2 +  (A[1] - C[1])**2 ) == ((A[0] - D[0])**2 +  (A[1] - D[1])**2 ) ==  ((B[0] - C[0])**2 +  (B[1] - C[1])**2 ) ==   ((B[0] - D[0])**2 +  (B[1] - D[1])**2 )!= 0  
        lst = [p1, p2, p3, p4]
        
            
        for i in range(4):
            for j in range(i+1, 4):
              
                if dfs(lst[i], lst[j]):
                    
                    return True
        return False
       