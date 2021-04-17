
class Solution(object):
    def cleanRoom(self, robot):
        """
        1) backtracking
        2) visted
        strategy: always trun right
        3) stop: try 4 paths
        4) expore, go back and turn right
        """
        v = set()
        def back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(cell, d ):
            v.add(cell)
            robot.clean()
            for i in range(4):
                news = (d+i) % 4
                newx, newy = cell[0] +dirs[news][0], cell[1] +dirs[news][1]
                if (newx, newy) not in v and robot.move():
                    dfs((newx,newy), news)
                    back()
                
                robot.turnRight()
        dirs =  [(-1,0),(0,1),(1,0),(0,-1)]
        dfs((0,0),0)
            