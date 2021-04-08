class Solution(object):
    def insert(self, intervals, newInterval):
        """
        [[1,3],[6,9]]
        [2,5]
        
       rt: cur.end < new.start 
       merge: overlap, 
       lf: new.end < cur.start
       
        """
        rt, lf = [],[]
        for e in intervals:
            if e[1] < newInterval[0]:
                lf.append(e)
            elif newInterval[1] < e[0] :
                rt.append(e)
            else:
                newInterval = [min(newInterval[0],e[0]), max(newInterval[1],e[1])]
        return lf + [newInterval] + rt
    def insert3(self, intervals, newInterval):
        """
        [[1,3],[6,9]]
        [2,5]
        
        [1,3] [2,5] [6,9]
        insert idx, where valofidx.start  > newInterval.start
        
         [1,3] [2,5] [6,9]
         at the begin res = [[1,3]]
         if res[-1].end < now.end, update the last on res
         else:
            append res
        """
        if not intervals:
            return [newInterval]
        pos  = 0 
        while pos < len(intervals):
            if intervals[pos][0] > newInterval[0]:
                break
            pos += 1
        intervals = intervals[:pos] + [newInterval] + intervals[pos:]
        
        res = [intervals[0]]
        # [[1, 2], [3, 5], [4, 8], [6, 7], [8, 10], [12, 16]]
        for e in intervals[1:]:
            if res[-1][1] >= e[0]:
                res[-1][1] = max(res[-1][1], e[1])
            else:
                res.append(e)
        return res
        
        def insert2(self, intervals, newInterval):
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
        
        