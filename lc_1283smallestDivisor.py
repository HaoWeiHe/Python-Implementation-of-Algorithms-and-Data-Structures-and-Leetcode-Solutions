class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        result = 
        sum of 
        q,r = divmod(m,n) return q + 1 if r else q
        
        smallest result <= threshold
        
        boundary :
        (1, 6)
        """
        l, r= 1, max(nums) + 1
        
        def result(d):
            res = 0 
            for num in nums:
                q,r = divmod(num,d)
                res += (q + 1) if r else q
            return res
        
        while l < r :
            mid = (l + r) / 2
            if result(mid) <= threshold:
                r = mid
            else:
                l = mid  +1
        return l
        
        