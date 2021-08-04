class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] *(n+1)
        if n == 2:
            return 1
        if n ==3:
            return 2
        if n ==4:
            return 4
        for i in range(2,5):
            dp[i] = i
        for i in range(2, n+1):
            for j in range(2, i/2 + 1):
                
                dp[i] = max(dp[i], dp[i-j]*dp[j])
        return dp[n]