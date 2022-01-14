class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        m,n = len(rooms), len(rooms[0])
        
        
        def bfs(i,j,v):
            q = deque([(i,j,0)])
            while q:
                x,y, step  = q.popleft()
                if (x,y) in v:
                    continue
                v.add((x,y))
                rooms[x][y] = min(rooms[x][y],step)
                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < m and 0 <= ny < n and rooms[nx][ny] > 0):
                        continue
                    q.append((nx,ny, step + 1))
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    bfs(i,j,set())
                   
    
       
                
                