class Solution(object):
    def longestCommonPrefix(self, strs):
        """
         ["flower","flow","flight"]
res =      "flower","flo", "fl"
        """
        if not strs:return ""
        res = strs[0]
        
        for w in strs[1:]:
            length = min(len(w), len(res))
            i = 0 
            res = res[:length]
            while i < length:
                if res[i] != w[i]:
                    res = w[:i]
                    break
                i +=1
                
                
        return res
                
        