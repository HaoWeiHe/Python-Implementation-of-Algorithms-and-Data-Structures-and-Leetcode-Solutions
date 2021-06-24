from collections import Counter
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        [3,4,2]
        [3,4,2]
        {3:1, 4:1,2:1}
        choice: 4  -> [2]
        choice: 3 - > [0]
        choice 2: [4]
        
        [2,2,3,3,3,4]
        
        {2:2, 3:3, 4:4}
        
        all - around
        
        
        [1,1,1,2,4,5,5,5,6] {1:3, 2:1, 4:1, 5:3, 6:1}
        -> 1  visted= [1,2]
            -> 4,5,5,5,6  
                -> 4 : [1,2,4,5]
                -> 5 :15 -> [1,2,4,5,6]
                -> 6 : 
        -> 2 : dfs[4,5,5,5,6]
            
        -> 4 :dfs( [1,1,1,2,6])
       
        
       
        """
        self.mem = {}
        def dfs(lst,visited):
            
            if len(lst) == len(visited):
                return 0
            tlst = tuple(visited)
            
            if tlst in self.mem:
                return self.mem[tlst]

            ans = 0
            orignal = { e for e in visited}
            for e in lst: 
                if e in visited:
                    continue
                
                visited.add(e)
                
                if e + 1 in lst:
                    visited.add(e + 1)
                
                if e - 1 in lst:
                    visited.add(e - 1)
                
                ans = max(ans, dfs(lst, visited) + lst[e]*e )
                visited = orignal
            self.mem[tlst] = ans
            return ans

        return dfs(Counter(nums), set())