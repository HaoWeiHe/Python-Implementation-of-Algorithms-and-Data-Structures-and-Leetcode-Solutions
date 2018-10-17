class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        for n in nums:
            if not res or n > res[-1][-1]+1:
                res += ([],)
            res[-1][1:] = (n,)
        return (['->'.join(map(str, i)) for i in res])