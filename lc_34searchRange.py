
class Solution(object):
    """
    find the idx makes all num >= target after num[idx]
    """
    def searchRange(self, nums, target):
        res = [-1,-1]
        if not nums: return res
        def helper(flag):
            l, r  = 0, len(nums)
            while l  < r:
                mid = (l+r) //2
                if nums[mid] > target or (flag and nums[mid] == target) :
                    r = mid
                else:
                    l = mid + 1
            return l 

        l = helper(True)
        if l < len(nums) and nums[l] == target:
            res[0] = l 

        l = helper(False)
        if  l > 0 and nums[l-1] == target:
            res[1] = l - 1
        
        return res

    def searchRange1(self, nums, target):
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
Solution().searchRange()