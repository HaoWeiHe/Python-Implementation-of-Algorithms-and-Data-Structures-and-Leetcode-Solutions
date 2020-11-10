class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0, len(h) -1
        res = 0
        while l <= r:
            area = min(h[l], h[r]) * (r-l)
            res= max(res,area)
            if h[l] > h[r]:
                r -=1
            else:
                l +=1
        return res
            