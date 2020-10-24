
import collections
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: 
            return 0
        m,n = len(grid), len(grid[0])
        dis_table = [[[float('inf'),0]]*n for _ in range(m)] 
        buildingNumer = 0
        for i in range(m):
            for j in range(n):
                    if grid[i][j] == 0:
                        dis_table[i][j] = [grid[i][j],0]
                    if grid[i][j] == 1:
                        buildingNumer +=1
              
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = collections.deque()
                    q.append((i,j,0))
                    s = set()
                    while  q:
                        x, y, lvl = q.popleft()
                        for dx, dy in [[0,-1],[0,1],[-1,0], [1,0]]:
                            nx, ny = x + dx , y + dy
                            if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in s:
                                if grid[nx][ny] == 0:
                                    dis_table[nx][ny][0] +=  lvl +1
                                    dis_table[nx][ny][1] += 1
                                    q.append((nx,ny , lvl +1))
                                    s.add((nx,ny))
        
        res = float('inf')
       
        for i in range(m):
            for j in range(n):
                if dis_table[i][j][1] == buildingNumer:
                    res = min(res, dis_table[i][j][0])
                  
       
        return res if res > 0 and res != float('inf') else -1

grid = [
[1,0,2,0,1],
[0,0,0,0,0],
[0,0,1,0,0]]
grid = [[1]]
grid = [
[0,2,1],
[1,0,2],
[0,1,0]]

# grid = [
# [1,1,1,1,1,0],
# [0,0,0,0,0,1],
# [0,1,1,0,0,1],
# [1,0,0,1,0,1],
# [1,0,1,0,0,1],
# [1,0,0,0,0,1],[0,1,1,1,1,0]]

print(Solution().shortestDistance(grid),"ew")