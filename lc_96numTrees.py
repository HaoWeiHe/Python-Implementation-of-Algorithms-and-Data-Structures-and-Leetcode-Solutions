class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return n
        dp = [1,1,2]
        for i in range(3, n+1):
            tmp = 0 
            for j in range(i): #0 1 2
                #i = 3 -> j = 0 1 2
                tmp += dp[j]*dp[i-j-1]
               
            dp.append(tmp)
       
        return dp[-1]
                
        