class Solution(object):
    def getFood(self, grid):
        """
        1. find the locate coordinate as first ele in queue
        2. bfs, and if accounter to food, return 
        """
        m,n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    locate = [i,j]
        q = deque([[locate[0], locate[1],0]])
        v = set()
        while q:
            x,y, step = q.popleft()
            
            if (x,y) in v:
                continue
            v.add((x,y))
            if grid[x][y] == "#":
                return step
            for dx, dy in [[0,1],[-1,0],[0,-1], [1,0]]:
                nx, ny = x + dx, y + dy 
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == "X":
                    continue
                q.append([nx,ny, step + 1])
        return -1