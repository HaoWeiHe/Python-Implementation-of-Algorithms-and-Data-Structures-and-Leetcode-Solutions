class Solution(object):
    def merge(self, intervals):
        """
         [[1,9],[2,6],[8,10],[15,18]]
         1) sort ele[0]
         2) for i in range(n):
            if n >= after[0] merge
        [1,(6,9)]
        1,9
        1,10
        """
        its = sorted(intervals, key = lambda x:(x[0],x[1]))
        n = len(its)
        cur_iterval = its[0]
        
        res = []
        for i in range(1,n):
            if cur_iterval[1] >= its[i][0]:
                cur_iterval[1] = max(its[i][1],cur_iterval[1] )
            else:
                res.append(cur_iterval)
                cur_iterval = its[i]
     
        res.append(cur_iterval)
        return res
            