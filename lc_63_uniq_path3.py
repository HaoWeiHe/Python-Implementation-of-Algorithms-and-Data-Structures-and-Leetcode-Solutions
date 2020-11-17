class Solution(object):
    def uniquePathsWithObstacles(self, g):
        if not g: 
            return 0
        if g[0][0] == 1:
            return 0
        m, n = len(g), len(g[0])

        flag = True
        for i in range(m):
            if g[i][0] == 0 and flag:
                g[i][0] = 1   
            else:
                flag = False
                g[i][0] = 0

        flag = True
        for j in range(1,n):
            if g[0][j] == 0 and flag:
                g[0][j] = 1 
                
            else:
                flag = False
                g[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if g[i][j] ==0:
                    g[i][j] = g[i-1][j] + g[i][j-1]
                else:
                    g[i][j] = 0
      
        return g[-1][-1]

    def uniquePathsWithObstacles2(self, g):
        """
        
        f(x,y) = f(x-1,y) + f(x, y-1)
       
        """
        if not g: 
            return 0
        if g[0][0] == 1:
            return 0

        m, n = len(g), len(g[0])
        dp = [[0] * n for _ in range(m)]
        
        flag = True
        for i in range(m):
            if g[i][0] == 0 and flag:
                dp[i][0] = 1   
            else:
                flag = False
                dp[i][0] = 0

        flag = True
        for j in range(n):
            if g[0][j] == 0 and flag:
                dp[0][j] = 1 
                
            else:
                flag = False
                dp[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if g[i][j] ==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
 
        return dp[-1][-1]

        
    def uniquePathsWithObstacles3(self, g):
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

        