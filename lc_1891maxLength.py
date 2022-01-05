# class Solution:
#     def maxLength(self, ribbons: List[int], k: int) -> int:
#         s = sum(ribbons)             # impossible case: when total length sum of all ribbons are less than `k`
#         if s < k: return 0
#         n = len(ribbons)
#         def ok(mid):                 # is it `ok` to form `k` ribbon with length `mid`?
#             nonlocal ribbons, k
#             cnt = 0
#             for r in ribbons:
#                 cnt += r // mid
#             return cnt >= k    
#         l, r = 1, max(ribbons)
#         while l <= r:                # binary search
#             mid = (l+r) // 2
#             if ok(mid):
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return r                
    
    
class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        def valid(mid):
            c = 0 
            for e in ribbons:
                c += e //mid
            return c >= k
            
        lo, hi = 1, max(ribbons) + 1
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if valid(mid):
                lo = mid +1
            else:
                hi = mid -1
        
        return hi if 0 <= hi <= max(ribbons) else 0