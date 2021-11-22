from heapq import heappush, heappop
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        [1,7,11], nums2 = [2,40,60]
             ^
                                ^
        """
        h = []
        for a in nums1:
            for b in nums2:
                heappush(h,(a+b,(a,b)))
        
        ans = []
        for _ in range(k):
            if not h:
                break
            _,ele = heappop(h)
         
            ans.append([ele[0],ele[1]])
        return ans