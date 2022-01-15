class Solution:

    # def longestPalindromeSubseq(self, s):
    #     n = len(s)
    #     dp_prev, dp = [0] *n, [0] * n 
    #     for l in range(1, n + 1):
    #         for i in range( n - l + 1):
    #             j = i + l - 1
    #             if i == j:
    #                 dp[i]= 1
    #                 continue
    #             if s[i] == s[j]:
    #                 dp[j] = dp_prev[j - 1] + 2
    #             else: 
    #                 dp[j] = max(dp_prev[j], dp[j - 1])
    #         dp_prev, dp = dp, dp_prev
    #     return dp_prev[n-1]
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] *n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n ):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else: 
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n-1]


    def longestPalindromeSubseq6(self, s):
        """
        bbbab
        v   v 1
         vv 
          vv
         bab
         bb
        """
        self.v = {}
        def dfs(i,j):
            
            if (i,j) in self.v:
                return self.v[(i,j)]
            if i > j :
                return 0
            if  i == j :
                return 1
            
            if s[i] == s[j]:
                self.v[(i,j)] = 2 + dfs(i + 1, j - 1)
            else:
                self.v[(i,j)] = max(dfs(i + 1, j), dfs(i, j - 1))   
            return self.v[(i,j)] 
        return dfs(0, len(s) - 1) 
        