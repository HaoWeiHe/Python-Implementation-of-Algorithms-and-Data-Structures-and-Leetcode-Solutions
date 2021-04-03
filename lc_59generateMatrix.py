class Solution(object):
    def generateMatrix(self, n):
        """
        (r1,c1) 
        
                    (r2,c2)
        top: (r1,c), c:(c1,c2)
        rt:  (r,c2), r:(r1+1, r2)
        btm: (r2,c), c:(c2-1, c1)
        lf:  (r,c1), r:(r2-1, r1+1) 
        
        """
        def helper(r1,c1,r2,c2):
            for c in range(c1,c2+1):
                yield (r1,c)
            for r in range(r1+1,r2+1):
                yield (r,c2)
                
            if r1==r2 and c1==c2:
                return 
            for c in range(c2-1, c1-1, -1):
                yield (r2,c)
                
            for r in range(r2-1, r1, -1):
                yield (r,c1)
        
        r1, c1, r2, c2 = 0,0,n-1,n-1
        res = [[0]*n for _ in range(n)]
        v = 1
        while r1 <= r2 and c1 <= c2:
            for x,y in helper(r1,c1,r2,c2):
                res[x][y] = v
                v +=1 
            r1 +=1 
            c1 +=1
            r2 -= 1
            c2 -=1
        return res
    