class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        instructions = instructions*4
        locs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0 
        x,y = 0,0
        re = set()
        for e in instructions:
            if e == "L":
                idx = (idx+3)%4
            elif e == "R":
                idx = (idx + 1)%4
            else:
                x += locs[idx][0]
                y += locs[idx][1]
            cur = tuple((x,y))
            
            
        return (x==0 and y == 0 ) or idx != 0 