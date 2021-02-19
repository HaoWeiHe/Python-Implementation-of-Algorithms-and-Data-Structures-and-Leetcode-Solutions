class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
       "abcabcbb"
         v
           v
        """
        if not s:
            return 0
        cs = {}
        i = 0 
        res = 0 
        for j, cur in enumerate(s): 
            if cur in cs:
                i = max(i,cs[cur])
            res = max(res, j - i + 1)              
            cs[cur] = j + 1
        return res

s = "abba" #a:1, b:2 b:2
print(Solution().lengthOfLongestSubstring(s))