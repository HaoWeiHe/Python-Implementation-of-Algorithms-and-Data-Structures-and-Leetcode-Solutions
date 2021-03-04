class Solution(object):
    def spiralOrder(self, m):
        """
        (r1,c1) - (r2,c2)
        
        top: (r1, c), c: (c1,c2)
        rt: (r, c2), r : (r1+1, r2)
        btm: (r2, c), c: (c2-1, c1 )
        lf:  (r, c1), r from (r2-1, r1+1)
        """
        def helper(r1,c1,r2,c2):
            for c in range(c1, c2+1):
                yield (r1,c)

            for r in range(r1+1, r2+1):
                yield (r,c2)

            if r1 == r2 or c1 == c2: return
            for c in range(c2-1, c1-1,-1):
                yield (r2,c)
            
            for r in range(r2-1,r1,-1):
                yield (r,c1)
            
        
        res = []
        r1,c1, r2,c2 = 0,0, len(m)-1, len(m[0])-1
        
        while r1 <= r2 and c1 <= c2:
            for x, y in helper(r1,c1,r2,c2):
                res.append(m[x][y])
            r1 +=1
            r2 -=1
            c1 +=1
            c2 -=1
        return res
    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []
        while 1:

            res.extend(matrix[0])
            matrix = matrix[1:]
            if len(matrix) == 0:
                break
            matrix = numpy.rot90(matrix)
            
        return res
