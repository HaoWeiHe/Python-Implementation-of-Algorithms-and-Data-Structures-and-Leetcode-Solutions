class Solution(object):
    def countSquares(self, g):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        g = [[0]+e for e in g ]

        g = [[0]*len(g[0])]+g
        m , n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                if g[i][j]:
                    g[i][j]= min(g[i-1][j], g[i-1][j-1], g[i][j-1])+1
        return sum([sum(e) for e in g])
        
