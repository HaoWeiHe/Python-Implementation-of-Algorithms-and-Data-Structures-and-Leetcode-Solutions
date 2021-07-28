class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        g [1,2,3,4,5]
        c [3,4,5,1,2]
               v
                 4
 tank               tank -c[i-1] + g[i]
                    4 - 1 + 5 = 8
                    8 - 2 + 1 = 7
             7 -3 +2 = 6
                6-4+3 = 5
                  5 - 5 ok!                
      g  [5,1,2,3,4]
      c  [4,4,1,5,1]
                v
tank              4
         4 -1 + 5 = 8
            8 - 4 + 1 = 5
              5 - 4 + 2 = 3
                3 - 1 + 3 = 5              
  
        """
        def f(tank, idx):
            n = len(cost)
            i = idx + 1
            
            while (i) % n != idx:
                
                tank = tank - cost[(i-1)%n] + gas[(i)%n]
                
                if tank - cost[(i)%n] < 0 :
                    return 0
                
                i += 1
            return 1
        for idx in range(len(gas)):
            tank = gas[idx]
            
            if tank < cost[idx]:
                continue
            if f(tank, idx):
                return idx
        return -1