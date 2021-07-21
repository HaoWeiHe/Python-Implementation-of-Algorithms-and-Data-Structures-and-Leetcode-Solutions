class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        1 ---- 100
          [10,100]
          -> 11 
        1                                   100
        ----|-
            10,60  ,[20,30],[30,30],[60,40]]
            (0:10):
            (1,70)
                    (0,70):1 -> (1,70), (2,100) 
                    (1, 100):2#
                            (1,70)
                            (2,100)# 
                                      (1,70)
                                      (2, 110) #
        """
        self.mem = {}
       
        self.ans = float('inf')
        def dfs(i, stop, howfar):
            if howfar >= target:
                return stop
            if (i, stop, howfar) in self.mem:
                return self.mem[(i, stop, howfar)]
            tmp = float('inf')
            for idx, ele in enumerate(stations[i:]):
                loc, fuel = ele
                if loc <= howfar: 
                    tmp = min(tmp, dfs(idx + i + 1, stop + 1, howfar + fuel), dfs(idx + i + 1, stop, howfar ))
            self.mem[(i, stop, howfar)] = tmp
            return tmp
        
        stops = dfs(0,0,startFuel)
       
        
        return stops if stops!= float('inf') else -1
            
            
            