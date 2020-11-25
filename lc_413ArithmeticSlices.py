class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        dp[i] = dp[i-1] + 1 if follow the rule
        
        """
        
        dp = [0]*len(A) 
        res = 0
        for i in range(2,len(A)):
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]):
                dp[i] = dp[i - 1] + 1;
            res += dp[i]
      
        return res
    
    def numberOfArithmeticSlices2(self, A):
        """
        
        [7, 7, 7, 1, 3, 5, 7, 9]
    gap [_, 0, 0,-6 2  2  2. 2 ]
        
        length = 1+2+3+.. + n-2 = (n-1)*(n-2)/2
            
        """
        def counter(tmp_len):
            return  (tmp_len-1) * (tmp_len-2)/2
        
        res, tmp_len = 0,   2
        for i in range(2,len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                tmp_len += 1
            else:
              
                if tmp_len >2:
                    res += counter(tmp_len)
                
                    tmp_len = 2
        if tmp_len > 2:
            res += counter(tmp_len)
        return res
        
        
