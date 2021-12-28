class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        3/4 + 6/4 + 7/4 + 11/4 <= 8
        0 + 1 + 1+1 + 1 + 1 + 2 + 1 if %!=0
        
        """
        if len(piles) > h:
            return -1
        
        left, right = 1, max(piles) + 1
        def valid(k):
            ans = 0 
            for p in piles:
                q,r = divmod(p, k)
                ans += q if r == 0 else q + 1
            return True if ans <= h else False
            
        while left < right:
            mid = (left + right) / 2
            if not valid(mid):
                left = mid + 1
            else:
                right = mid
        return left