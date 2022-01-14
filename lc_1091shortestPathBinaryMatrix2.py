class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if not grid or grid[0][0]!= 0 or grid[m-1][n-1] != 0 :
            return -1
        q = deque([(0,0,1)]) #i,j, step
        v = set()
        while q:
            x, y, step = q.popleft()
            if (x,y) == (m-1, n-1):
                return step
            if (x,y) in v:
                continue
            v.add((x,y))
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                nx, ny = x + dx, y + dy 
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0):
                    continue
                q.append((nx,ny,step+1))
        return -1