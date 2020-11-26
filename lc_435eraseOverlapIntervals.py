class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """

        """
        intervals.sort()
        if len(intervals) <=1:
            return 0
    
        l,r = 0,1
        count = 0
        while r < len(intervals):
            if intervals[l][1] <= intervals[r][0]:
                l = r
               
            elif intervals[l][1] <= intervals[r][1]: #del right
                count +=1
               
            else:
                count +=1
                l = r
            r +=1
            
        return count
                
            