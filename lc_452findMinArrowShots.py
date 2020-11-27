class Solution(object):
    def findMinArrowShots(self, points):
        """
        [[1, 6], [2, 8], [7, 12], [10, 16] , [11,]]
         (1,6)  (2,6)    (7,12,1) (10,12,2)
                 1 < 2(start)< 6       7< 10<12
        """
        points.sort()
        count = 1
        if not points:
            return 0
        l,r = points[0]
        for e in points[1:]:
            start, end = e
            if l <= start <= r:
                l,r = max(l, start), min(r, end)
            else:
                l,r = start, end
                count +=1
        return count
            