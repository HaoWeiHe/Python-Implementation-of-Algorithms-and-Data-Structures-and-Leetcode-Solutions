class Solution(object):
    def isRobotBounded(self, instructions):
        """
        iff bounded in circle:
        1) return to the orignal coodination
        2) change its direction (this will couse back to orignal after few rounds)
        """
        move = [(0,1),(-1,0), (0,-1),(1,0)]
        i,j, direction = 0, 0 , 0
        for ele in instructions:
            if ele == "G":
                dx, dy = move[direction]
                i += dx
                j += dy
            elif ele == "L":
                direction = (direction +1) %4
            else:
                direction = (direction -1) %4
        return (i,j) ==(0,0) or direction!= 0
        