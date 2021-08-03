class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = 0
        for e in nums:
            if e == 0:
                return 0
            if e < 0:
                s += 1
                
     
        return 1 if s%2 ==0 else -1
        