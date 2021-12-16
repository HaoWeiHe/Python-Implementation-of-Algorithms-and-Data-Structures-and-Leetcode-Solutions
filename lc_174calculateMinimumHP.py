class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        inf = float('inf')
        dungeon = [row + [inf] for row in dungeon]
        dungeon +=  [[inf] * len(dungeon[0])]
       
        m,n = len(dungeon), len(dungeon[0])
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if i == m-2 and j == n-2:
                    dungeon[i][j] = 1 + abs(dungeon[i][j]) if dungeon[i][j] <= 0 else 1
                    continue
                down, right, cur = dungeon[i][j+1], dungeon[i+1][j], dungeon[i][j]
                dungeon[i][j] = min(max(1, down - cur ), max(1, right - cur))
        return dungeon[0][0]
    def calculateMinimumHP2(self, dungeon):
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