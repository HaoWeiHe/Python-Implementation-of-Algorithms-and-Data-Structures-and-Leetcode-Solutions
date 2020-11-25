class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        dfs to check every possible intervals
        """
    
        def check(intervals):
            n = len(intervals)
            for i in range(n):
                for j in range(i+1, n):
                    a_start, a_end = intervals[i]
                    b_start, b_end  = intervals[j]
                    if a_start <= b_start <= a_end and a_start <= b_end <= a_end:
                        return False
            return True

        # pop one of them

        self.res =[]
        self.visted = []
        def gen(intervals):
            
            cur = "".join(map(str, intervals))
            print(cur,intervals)
            if cur not in self.visted:
                self.res.append(intervals)
            self.visted.append(cur)
            tmp = intervals[:] 
            for ele in intervals:
                tmp.remove(ele)
                gen(tmp)
                tmp.append(ele)
        
        gen(intervals)
        for e in self.res:
            print(e,"Re")
        candidates = sorted(self.res, key = lambda x: len(x), reverse = True)
        # for ele in candidates:
        #     print(ele)
            # if check(ele):
                # return len(intervals) - len(ele)
      
intervals =  [[1,2],[2,3]]#[[1,2],[2,3],[3,4],[1,3]]
print(Solution().eraseOverlapIntervals(intervals))