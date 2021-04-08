class Solution(object):
    def insert(self, intervals, newInterval):
        """
       1) insert newInterval into 
       2) merge this intervals
       
       [1,3] [2,5] [6,9]
             v
        
       [[1,2],[4,8], [3,5],[6,7],[8,10],[12,16]], 
               v
               
        [[1,2],[4,8], [3,5],[6,7],[8,10],[12,16]]
        
         [[1,2],[4,8], [3,5],[6,7],[8,10],[12,16]]
          [[1,2],[3,8],[6,7],[8,10],[12,16]]
          [[1,2],[3,8],[8,10],[12,16]]
          [[1,2],[3,10],[12,16]]
        """
        if not intervals: return [newInterval]
        insert_i = 0
        while insert_i < len(intervals):
            e = intervals[insert_i]
            if newInterval[0] < e[1]:
                break
            insert_i+=1 
        
        intervals = intervals[:insert_i]  +  [newInterval ] + intervals[insert_i:]
        res= [intervals[0]]
        def overlap(a,b):
            if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
                return True, [min(a[0],b[0]), max(a[1],b[1])]
            return False, None
        
        for e in intervals[1:]:
            flag, val = overlap(e, res[-1])
            if flag:
                res[-1] = val
            else:
                res.append(e)
        return res
        
        