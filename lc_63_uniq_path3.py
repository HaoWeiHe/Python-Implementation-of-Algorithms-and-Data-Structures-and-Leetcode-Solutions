class Solution(object):
    def uniquePathsWithObstacles(self, g):
        """
        
        f(x,y) = f(x-1,y) + f(x, y-1)
       
        """
        m, n = len(g), len(g[0])
        self.mem ={}
        
        def f(x,y):
          
            if x < 0 or y < 0 : 
                return 0
            if x == 0 and y == 0:
                return 1 * int(g[x][y] ==0)
            if (x,y) in self.mem :
                return self.mem[(x,y)]

            self.mem[(x,y)] =  (f(x-1,y) + f(x,y-1)) * int(g[x][y] ==0 )
            
            return self.mem[(x,y)]

        return f(m-1,n-1)

        