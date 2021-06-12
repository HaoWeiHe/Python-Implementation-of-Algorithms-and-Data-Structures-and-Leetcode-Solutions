class Solution(object):
    def climbStairs(self, n):
        """
        dp[i] = dp[i-1] + dp[i-2]
        cur = prev1 + prev_2
        prev1 = cur
        prev2 = prev1
        
        n == 0 : 0
        n == 1: 1
        n == 2: 2
        
        """
        if n < 3:
            return n
        cur, prev1, prev2 = 0,2,1
        for i in range(3, n+1):
            cur = prev1 + prev2  # 3 = prev1 = 1
            prev1, prev2 = cur, prev1
        return cur
        