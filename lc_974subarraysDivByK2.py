class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        sum[i:j] = presum[0:j] - presun[0:i]
        
        sum[i:j] %k == 0, means 
        presum[0:j] %k ==  presun[0:i]%k
        
        -> would like to know how many presun[0:i]%k shown before (we can make a started point from all of them)
        
        [4,5,0, -2,-3,1]
         v
        k = 5
        
        presume = 4
        ans = 0
        (4:1)
        presume = 4
        ans = 1
        presume = 4
        (4:2) -> there are 2 numbers whose remind == 4
        ans = 3
        presume = 2
        (4:2, 2:1)
         
        """
        history = defaultdict(int)
        history[0] = 1
        presum, ans = 0, 0
        
        for e in nums:
            presum += e
            ans += history[presum%k]
            history[presum%k] += 1
            
        return ans 
        