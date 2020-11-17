class Solution(object):
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
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        
        res = float('inf')

        for i in range(1,len(triangle)):
            for j  in range(i+1):
                top, left = float('inf'),float('inf')
                if 1 < j  :
                    left = triangle[i-1][j-1]
                if j < i+1:
                    top = triangle[i-1][j]
        
                triangle[i][j] = triangle[i][j] + min(left, top)    
                # triangle[i][j] = triangle[i][j] + min(triangle[i-1][j], triangle[i-1][j-1])
        print(triangle)
        for e in triangle:
            print(e)
        return min(triangle[-1])

    def minimumTotal2(self, triangle):
        
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
            self.res = min(self.res, f(m-1,j))
            
        return self.res
 

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

for e in triangle:
    print(e)
print(Solution().minimumTotal(triangle))