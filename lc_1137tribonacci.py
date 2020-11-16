class Solution(object):
    def tribonacci(self, n):
        """
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

        """
        if n == 0: return 0
        if n < 3: return 1
        dp = [0] * max(3,n+1)

        a, b, c = 0,1,1  #dp[0], dp[1], dp[2] = 0,1,1

        for i in range(3,n+1):
            c, b, a = c + b + a, c ,b #dp[i-1] + dp[i-2] + dp[i-3]

             
        return c

    def tribonacci2(self, n):
        """
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

        """

        dp = [0] * max(3,n+1)

        dp[0], dp[1], dp[2] = 0,1,1

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]

            
    def tribonacci2(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.memo = {}
        def T(n):
            if n ==0: return 0
            if n < 3: return 1
            if n in self.memo : 
                return self.memo[n]
            self.memo[n] = T(n-1) + T(n-2) + T(n-3)
            return self.memo[n]
        return T(n)

n = 30
print(Solution().tribonacci(n))