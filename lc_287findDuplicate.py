class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = set()
        for e in nums:
            if e in h: return e
            h.add(e)
        