class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        l, r = min(bD), len(bD)
        f(days) >= m
        [x, x, x, x, _, x, x]
               ^
    acc  1  2  3  1  0  1  2
               %3 ==0-> b += 1
        
    
    bq = 1  1  1  2
    
    in the end, check if l is valid
    if not -1
        """

        l, r = min(bloomDay), max(bloomDay) + 1
        """
        [1,10,3,10,2]
         x    x    x if <= day
acc_num  1  0 1  0 1   
    ans = 1 1 2  0  3 
        day = 3  ans == m (True)

        """
        def valid(day):
            acc_num, ans = 0,0
            for ele in bloomDay:
                if  ele > day:
                    acc_num = 0
                    continue
                
                acc_num += 1
                if acc_num == k:
                    ans += 1
                    acc_num = 0 
            return ans >= m
         
        while l < r:
            mid = (l + r) / 2
            if valid(mid):
                r = mid
            else:
                l = mid +1
        
        return l if 0 <= l <= max(bloomDay) else -1
        