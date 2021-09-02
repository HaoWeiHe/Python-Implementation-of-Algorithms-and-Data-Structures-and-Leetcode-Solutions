class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(grid), len(grid[0])
        
        def get_area(i,j):
            res = []
            def helper(i,j,l):
                tmp = grid[i][j]
                for lg in range(1,l+1):
                    tmp  += grid[i+lg][j-lg]
                    tmp  += grid[i+lg][j+lg]
                    tmp += grid[i+l+lg][j-l+lg]
                    tmp += grid[i+l+lg][j+l-lg]
                if l >0:
                    tmp -= grid[i+2*l][j]
               
                return tmp
            
            for l in range(max(m,n)):
                if j- l < 0 or j + l >= n or i + 2*l >= m: continue
                res.append(helper(i,j,l) )
               
            return res
        h = []
        for i in range(m):
            for j in range(n):
                arealist  = get_area(i,j)   
                h += arealist
        
        return sorted(list(set(h)), reverse = True)[:3]