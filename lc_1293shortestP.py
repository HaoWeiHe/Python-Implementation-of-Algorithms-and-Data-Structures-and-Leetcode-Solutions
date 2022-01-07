class Solution(object):
    def shortestPath(self, grid, K):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        m,n = len(grid), len(grid[0])
        q = deque([[0,0,K,0]])
        mem = set()
        while q:
            x, y, k, step = q.popleft()
            
            if (x,y,k) in mem or k < 0:
                continue
                
            if (x,y) == (m-1, n-1) :
                return step
            
            mem.add((x,y,k))
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = dx + x , dy + y 
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == 1: 
                    q.append((nx,ny,k - 1, step + 1))
                else:
                    q.append((nx,ny,k, step + 1))
   
        return -1