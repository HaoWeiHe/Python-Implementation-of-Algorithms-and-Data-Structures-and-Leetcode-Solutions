class Solution(object):
    def minCost2(self, costs):
        """
       [[17,2,17],[16,16,5],[14,3,19]]
            1     not 1      
        """
        self.v = {}
        def dfs(idx, pre): #idx = next idex, pre = used color
            ans = float("inf")
            if idx == len(costs):
                return 0
            
            if (idx,pre) in self.v:
                return self.v[(idx,pre)]
            
            for c_idx in range(3):
                if c_idx == pre :
                    continue
                ans = min(ans,costs[idx][c_idx] + dfs(idx + 1, c_idx))
            self.v[(idx,pre)] = ans 
            return self.v[(idx,pre)]
        return dfs(0, 3)
    def minCost(self, costs):
        """
        [[17, 2, 17], [8, 4, 10], [6, 3, 19], [4, 8, 12]]
     i                 ^   
                                    [6 + min(8,12), 3 + min(4,12), 19 + min((4,8))]
        
        """
        
        n = len(costs)
        for i in range(n - 2,-1,-1):
            costs[i][0] = costs[i][0] + min(costs[i+1][1],costs[i+1][2]  )
            costs[i][1] = costs[i][1] + min(costs[i+1][0],costs[i+1][2]  )
            costs[i][2] = costs[i][2] + min(costs[i+1][1],costs[i+1][0]  )
            
        return min(costs[0])
            