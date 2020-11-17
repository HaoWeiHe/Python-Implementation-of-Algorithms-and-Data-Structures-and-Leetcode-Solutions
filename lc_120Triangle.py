class Solution(object):
    def minimumTotal(self, triangle):
        """
              [
             [2],  0
            [3,4], 0  1
           [6,5,7], 0,1  2
          [4,1,8,3]   1,2 3
        ]
        
        f(x,y) : the max value from left bottom to x,y
        f(x,y) = min(f(x-1,y) , f(x-1,y-1) ) + A[x][y]
        """
        self.res = float('inf')
        
        def f(x,y):
            if y > x:
                return float('inf')
            if x < 0 or y < 0:
                return float('inf')

            if x == 0 and y == 0:
                return triangle[0][0] 

            if (x,y) in self.mem :
                return self.mem[(x,y)]
    
            self.mem[(x,y)] =  min(f(x-1,y) , f(x-1,y-1) )  + triangle[x][y]
           
            return self.mem[(x,y)]

        m = len(triangle) 
        for  j in range(len(triangle[-1])):           
            self.mem  = {}
            tmp = f(m-1,j)
            self.res = min(self.res, tmp)
            
        return self.res
