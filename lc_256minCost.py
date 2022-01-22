class Solution(object):
    def minCost(self, costs):
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
            