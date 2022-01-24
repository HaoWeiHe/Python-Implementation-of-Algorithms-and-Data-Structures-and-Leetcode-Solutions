class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}#1:idx
        for idx, e in enumerate(nums):#[1,2,3,1]
            if e in d: #{1:0,2:1, 3:2,}
                if idx - d[e] <= k :
                    
                    return True
            d[e] = idx
        return False