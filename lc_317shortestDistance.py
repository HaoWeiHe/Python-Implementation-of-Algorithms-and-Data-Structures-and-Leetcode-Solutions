from collections import deque
class Solution(object):

    def shortestDistance2(self, grid):
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
    

    def shortestDistance(self, grid):
        m,n = len(grid), len(grid[0])
        num_house = 0 
        g = [[(0,0)] * n for _ in range(m)]
        
        def explore(x,y,v):
            q = deque([[x,y,0]])
            while  q:
                x,y, step = q.popleft()
                
                if (x,y) in v:
                    continue
                
                v.add((x,y))

                if grid[x][y] == 0:
                    g[x][y] = (g[x][y][0]+ 1, g[x][y][1]+ step)
                     

                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 :
                        q.append((nx,ny, step + 1))
                        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_house += 1 
                    explore(i,j,set())
                    
    

        ans = float("inf")
        for i in range(m):
            for j in range(n):
                if g[i][j][0] == num_house:
                    ans = min(ans, g[i][j][1])
        
        return -1 if ans == float("inf") else ans
