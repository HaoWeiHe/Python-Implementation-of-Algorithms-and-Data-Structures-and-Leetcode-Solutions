class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        info =  sorted( zip(startTime, endTime, profit), key = lambda x : x[1])
        
        dp  = [(0,0)]
        def bfs(target):
            l,r = 0, len(dp)
            while l < r:
                m = l + (r-l)/2
                if target < dp[m][0] :
                    r = m
                else:
                    l = m + 1
            return l -1
        
        for s, e, p in info:
            
            idx = bfs(s)
            if p + dp[idx][1] > dp[-1][1]:
                dp.append((e, p + dp[idx][1]))
#             if p + val_of_dp[nearest_start] > val_of_dp[-1]: update dp
        return dp[-1][1]