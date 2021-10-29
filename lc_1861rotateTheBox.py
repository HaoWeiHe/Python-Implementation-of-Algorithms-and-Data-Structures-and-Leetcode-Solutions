class Solution(object):
    def rotateTheBox(self, box):
        """
              
        [
        (0,0)
        ["#",".","*","."],
        ["#","#","*","."]
                         (m,n)
        ]
            
        [
             ["#","."],
             ["#","#"],
             ["*","*"],
             [".","."]
         ]
        """
        m, n = len(box), len(box[0])
        
        graph = [[0]*m for _ in range(n)]
        for i in range(m):
            stone = -1 
            for j in range(n):
                if box[i][j] == "." and stone != -1:
                    box[i][j], box[i][stone] = box[i][stone], box[i][j]
                    stone += 1
                
                elif box[i][j] == "#" and stone == -1:
                    stone = j

                elif box[i][j] == "*":
                    stone = -1
        
        for i in range(m):
            for j in range(n):
                graph[j][m-i-1] = box[i][j]
       
       
        return graph
        