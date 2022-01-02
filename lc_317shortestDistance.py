class Solution(object):
    def shortestDistance(self, grid):
        """
        [
        [x,x,2,x,1],
        [x,T,T,x,0],
        [0,x,x,x,0]
        ]
        steps: 1 2 3
        if == 1:
            ans += steps #ans = 4
            
        if == 0:
            append to node
        try every node
        bfs until all node is been visited 
        """
        self.steps, self.houseV = 0, 0 
        m,n = len(grid), len(grid[0])
        
        def getDistance(i,j,v):
            q = deque([(i,j,0)])
            while q:
                x,y, step = q.popleft()
                if (x,y) in v:
                    continue    
                v.add( (x,y))
                if grid[x][y] == 1:
                    self.steps += step
                    self.houseV += 1
                    
                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[x][y] != 2:
                        q.append((nx,ny,step + 1))
        house_should_v = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    house_should_v += 1
                    
        ans = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                self.steps = 0  
                self.houseV = 0 
                getDistance(i,j,set())
                if self.houseV != house_should_v :
                    continue
                ans = min(ans, self.steps)
        return ans if ans != float("inf") else -1
    
