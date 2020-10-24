class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        h = {}
        lf, res = 0,0
        for idx, val in enumerate(s):
            h[val]  = idx 
            if (len(h) > k):
                rm_idx = min(h.values())
                del h[s[rm_idx]]
                lf = rm_idx+1
            res = max(res, idx-lf+1)
        
        return res
        