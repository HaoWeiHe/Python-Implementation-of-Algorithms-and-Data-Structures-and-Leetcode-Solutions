class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        lst = []
        for i,v in enumerate(ranges):
            lst.append((i-v, i+v))
        lst.sort(key= lambda (x,y): (x,y))
        
        i, pre, end, ans = 0, 0, 0, 0
        
        while end < n:
            while i < n+1 and lst[i][0] <= pre:
                end = max(end, lst[i][1])
                i+=1
           
            if pre == end:
                return -1
            pre = end
            ans += 1
        return ans