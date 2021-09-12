class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if 0 not in stones:
            return False
        
        if 1 not in stones:
            return len(stones) == 1
            
        self.mem = {}
        
        endstone = stones[-1]
        def dfs(start, k):
            if start == endstone:
                return True
            if start > endstone:
                return False
            if (start, k) in self.mem :
                return self.mem[(start, k)]
            res = False
            
            for unit in [k -1, k, k + 1]:
                if unit == 0:
                    continue    
                if start + unit  in stones :
                    res = res or dfs(start+unit, unit)
            
            # if res == True:
            self.mem[(start, k)] = res
            return res

        res = dfs(1,1)
       
        return res 