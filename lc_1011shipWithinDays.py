class Solution(object):
    def shipWithinDays(self, ws, ds):
    #     """
    #     :type weights: List[int]
    #     :type days: int
    #     :rtype: int
    #     """
        left, right = max(ws), sum(ws) + 1
        while left < right:
            need, cur = 1, 0
            mid = (right + left) / 2
            for w in ws:
                if cur + w > mid:
                    cur = 0 
                    need += 1
                cur += w
            if need > ds:
                left = mid +1
            else:
                right = mid
        return left
    