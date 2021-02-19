class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
       "abcabcbb"
         v
           v
        """
        if not s:
            return 0
        cs = set()
        l,r = 0 , 0
        res = 0 #abcabcbb
        for cur_idx, cur in enumerate(s): 
            while cur in cs:
                
                cs.remove(s[l])        
                l +=1
            
            res = max(res, cur_idx - l + 1)  
            
            cs.add(cur)
        return res

    def lengthOfLongestSubstring2(self, s):
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
