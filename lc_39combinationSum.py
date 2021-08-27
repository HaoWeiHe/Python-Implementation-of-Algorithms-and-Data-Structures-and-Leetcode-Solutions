class Solution(object):
    def combinationSum(self, candidates, target):
        """
        [2,3,6,7]
        2 
            5
                2
                3
                6
                7
            
        3 
            4
              2
                > 2 
                here!
              3
               > 1
              6
                
              7
             
        6
            1
            nope
        7
            0 here!
    
        2,3,3
        
        """
        self.res = []
        self.his = set()
        
        def dfs(num, record):
            
            if num == 0:
                
                self.res.append(record)
                
                return 
            if num < 0:
                return
            for e in candidates:
                if record and e < record[-1]:
                    continue
                dfs(num-e,record +[e])
        dfs(target,[])
        return self.res
            