class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        find min(abs(x) )
        -8,-2 -> 2!
        2,3 -> 1
        """
        self.ans = float('-inf')
        m,n = len(dungeon), len(dungeon[0])
        
        if not dungeon:
            return 1
        
        def dfs(x,y,h_score, mn_in_trip):
            
            if x == m-1 and y == n-1: 
             
                self.ans = max(self.ans, mn_in_trip)
                return 
            
            for dx, dy in [(0,1),(1,0)]:
                nx, ny  = x + dx, y + dy 
                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue
                
                dfs(nx, ny, h_score + dungeon[nx][ny], min(mn_in_trip, h_score + dungeon[nx][ny]))
            
        dfs(0,0,dungeon[0][0], dungeon[0][0])
        
        return 1 if (self.ans > 0 or self.ans == float('-inf'))  else abs(self.ans) + 1