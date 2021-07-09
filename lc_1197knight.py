class Solution(object):
    def minKnightMoves(self, x, y):
        """
        [0,0] (x2,x1) or (x1,x2)
        [2,1]
        
        [0,0]
        [2,1]
        [4,2]
        [3,4]
        1. abs(x,y)
        [4,2] -> (2, 1) or (-2, 1) or (1,2) or -1,2
        """
        x, y = abs(x), abs(y)
        q = deque([(0,0,0)])
        v = set()
        while q:
            i,j, level = q.popleft()
            if i > 2*x or j > 2*j:
                continue
            if (i,j) == (x,y):
                return level
           
            
            for dx, dy in [(2,1), (2,-1),(-2,1), (1,2), (-1,2),(1,-2)]:
                newx, newy = dx+i, dy +j
                if (newx, newy) in v:
                    continue
                v.add((newx, newy))
                q.append((newx, newy, level + 1))
                
                