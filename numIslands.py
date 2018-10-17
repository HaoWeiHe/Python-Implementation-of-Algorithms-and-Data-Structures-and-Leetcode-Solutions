class Solution:
    def numIslands(self, grid):
        
        if not grid:
            return 0
        
        count, max_x, max_y = 0 , len(grid),len(grid[0])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.dfs(grid,x,y,max_x, max_y)
                    count += 1
                    
        return count
    
    def dfs(self,grid,x,y, max_x , max_y  ):
        #if 1 than tag as 2
        if x >= max_x or y >= max_y or grid[x][y] !="1" or x < 0 or y < 0 :
            return 
        if grid[x][y] == "1":
            grid[x][y] = "2"
        
        self.dfs(grid,x+1,y,max_x, max_y )
        self.dfs(grid,x,y+1,max_x, max_y )
        self.dfs(grid,x-1,y,max_x, max_y )
        self.dfs(grid,x,y-1,max_x, max_y )
