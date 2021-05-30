class Solution(object):
    def removeStones(self, stones):
        """
        Question is asking about how many island are there
        #return number of stones - number of island
        
        """
        n = len(stones)
        g = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    g[tuple(stones[i])].append(tuple(stones[j]))
        
        def dfs(ele):
            self.v.add(ele)
            for nei in g[ele]:
                if nei in self.v:
                    continue
                dfs(nei)
            
            
        self.v = set()
        island = 0 
        for ele in stones:
            ele = tuple(ele)
            if ele in self.v:
                continue
            dfs(ele)
            island += 1
        return len(stones) - island