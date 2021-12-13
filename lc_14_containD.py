class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # s = set()
        # for e in nums:
        #     if e in s:
        #         return 1
        #     s.add(e)
        # return 0
        if not nums:
            return 0
        nums.sort()
        pre = nums[0]
        for e in nums[1:]:
            if e == pre:
                return 1
            pre = e
        return 0