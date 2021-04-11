class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        dp = [[float('-inf')]*n for _ in range(n)]
        
        def dfs(l,r):
            if l > r:return 0
            if l == r:return piles[l]
            if dp[l][r] == float('-inf'):
                dp[l][r] = max( piles[l] - dfs(l+1,r), -dfs(l,r-1) + piles[r])
            return dp[l][r]
            
            
        return dfs(0,len(piles)-1) > 0 