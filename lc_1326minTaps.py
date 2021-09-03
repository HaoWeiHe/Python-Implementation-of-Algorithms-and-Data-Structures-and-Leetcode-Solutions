

class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        lst = []
        for i in range(n+1):
            lst.append((i- ranges[i], i+ranges[i]))
        lst.sort(key = lambda x:(x[0],x[1]))
       
        if not lst:
            return -1

        ans, e, l, i = 0, 0, 0,  0
        
        
        while e < n: 
            while i <= n and lst[i][0] <= l:
                e = max(e, lst[i][1])
                i+= 1
                
            if e == l:
                return -1
            l = e
            ans += 1
        return ans