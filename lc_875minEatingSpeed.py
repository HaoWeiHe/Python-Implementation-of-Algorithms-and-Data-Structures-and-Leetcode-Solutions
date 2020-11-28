class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        [3,6,7,11]
         A B C D 
        ceil(A/k) + ceil(B/K) + ceil(C/K) + ceil(D/K) <= H
        find k to match this equation
        
        H guess between min(piles) to max(piles) 
        
        -> 3, 11
        slow -> max(all possible k)
        """
        l,r  = 1, max(piles)
        
        def vaild(k):
            k = float(k)
            res = 0
            for p in piles:
                res += math.ceil(p/k)
            return res <= H
        
        while l <= r:
            mid = (l + r) /2
            
            if vaild(mid):
                r = mid - 1
            else:
                l = mid + 1
    
        return l