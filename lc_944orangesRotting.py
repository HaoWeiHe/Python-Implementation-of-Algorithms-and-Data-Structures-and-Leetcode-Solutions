class Solution(object):
    def orangesRotting(self, g):
        """
        bfs, update until q is empty
        everyupdate 4 direction
        
        once finish, check if all orange tern to rotten
        """
        q = deque([])
        m,n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                if g[i][j] == 2:
                    q.append((i,j))
        ans = 0
        while q:
            ans += 1
        
            for _ in range(len(q)):
                
                top = q.popleft()
                g[top[0]][top[1]] = 2
                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    x,y = dx +top[0], dy + top[1]
                    if 0<=x < m and 0 <= y < n and g[x][y]==1 and (x,y) not in q:
                        q.append((x,y))
   
        for i in range(m):
            for j in range(n):
                if g[i][j] ==1:return -1
        return max(0,ans-1)