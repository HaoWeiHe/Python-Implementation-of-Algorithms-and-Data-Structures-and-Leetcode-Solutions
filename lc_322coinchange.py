class Solution(object):
    def coinChange(self, coins, amount):
        """
        1,2,5 return 1
        < 0 return inf
        3 -> 1,2
        5 -> 0+5, 2+3, 1+4
        mem[]
        4 = 2+2, 1+3
        check 2: 1
        1,2,5
        7 -> 5+2, 2+5, 1 + 6
        """
        self.mem = {}
        
        def dfs(rest):
            if rest == 0:
                return 0,1 
            if rest < 0 :
                return 0, 0
            
            if rest in coins:
                self.mem[rest] = 1
                return 1, 1
            
            if rest in self.mem:
                return self.mem[rest], 1

            ans = float('inf')
            for e in coins :
                v, work = dfs(rest -e)
                if work:
                    ans = min(1 +v ,ans)
            self.mem[rest] = ans
            
            return self.mem[rest],  ans != float('inf')
        
        rest, work = dfs(amount)
        
        return rest if work else -1

    def coinChange2(self, coins, amount):
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
        