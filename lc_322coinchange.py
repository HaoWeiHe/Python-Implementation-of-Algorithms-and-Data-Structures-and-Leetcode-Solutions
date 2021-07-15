class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.res  = float('inf')
        def dfs(rest,n):
            if rest < 0:
                return 
            
            if rest == 0 :
                self.res = min(self.res, n)
                return 
            for e in coins:
                dfs(rest-e, n  + 1)
        dfs(amount, 0)
        return self.res if self.res != float('inf') else -1
        