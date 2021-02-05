class Solution(object):
    def lengthOfLIS(self, nums):
        """
        [10,9,2,5,3,7,101,18]
          1 1 1 2 2 3  4   
        """
        h = {}
        for i,n in enumerate(nums):
            tmp = 0
            for ele in h:
                if ele < n:
                    tmp = max(tmp, h[ele])
            h[n] = tmp + 1
        
        return max(h.values())