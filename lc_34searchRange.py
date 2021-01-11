class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        for idx,e in enumerate(nums) :
            if e == target:
                if res[0] == -1:
                    res[0] = idx
                res[1] = idx
        return res