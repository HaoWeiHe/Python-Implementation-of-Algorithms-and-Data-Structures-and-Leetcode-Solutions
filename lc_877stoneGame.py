class Solution(object):
    def stoneGame(self, piles):
        """

        """
        memo = [[-1]*len(piles) for _ in piles] 
        def dfs(l,r):
            if l ==r:
                return piles[l]
            if memo[l][r]== -1:
                memo[l][r] = max(piles[l] -dfs(l+1,r), piles[r] - dfs(l,r-1))
            return memo[l][r]
        return dfs(0,len(piles)-1) > 0
        