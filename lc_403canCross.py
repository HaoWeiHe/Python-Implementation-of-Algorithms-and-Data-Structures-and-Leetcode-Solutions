class Solution(object):
    def canCross(self, stones):
        """
        map[idex] = (k1, k2,k3)
        [0,1,3,5,6,8,12,17]
         1
         h = {0:[1],1:[],3:[],5:[]}
         h = {e:defaultdict(list) for e in stones}
         
        """

        h = {e:set() for e in stones}
        h[0].add(0)
     
        for e in stones:
            for k in h[e]:
                for plus in range(-1,2):
                    if plus+k <= 0 or (e + k + plus) not in h:
                        continue
                    h[e + k + plus].add(k+plus)
        
        return len(h[stones[-1]]) > 0 
        
    def canCross2(self, stones):
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