from collections import defaultdict
class Solution(object):
    def largestIsland(self, grid):
        """
        g1: (0,0), (0,1).., g2:(2,0),(3,7)..
        (0,0) -> g1
        (0,1) -> g2
        d
        d_inverse
        find all ele == 0:
            it neighbiors  (0,0), (0,1)
            {g1, g2}
            then sum up (len(d[g1]), len(d[g2]))
        
        """
        d = defaultdict(list)
        d_inv = {}
        
        def traval(i,j,groupID):
            if (i,j) in d_inv:
                return 

            d[groupID].append((i,j))
            d_inv[(i,j)] = groupID
            
            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                nx, ny = i + dx, j + dy
                if 0 > nx or nx >= m or 0 > ny or ny >=n or (nx, ny) in d_inv or grid[nx][ny] == 0:
                    continue
                traval(nx,ny,groupID )
                
        gid = 0 
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in d_inv:
                    gid += 1
                   
                    traval(i,j, gid)

        
        ans, flag = 1, False
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                flag = True
                g = set()
                
                for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    nx, ny = i + dx, j + dy
                    if 0 > nx or nx >= m or 0 > ny or ny >=n or grid[nx][ny] == 0 :
                        continue
                    g.add(d_inv[(nx,ny)])
                    ans = max(ans,1 + sum([len(d[gid])for gid in g]))
        
        return ans if flag else len(grid) * len(grid)
