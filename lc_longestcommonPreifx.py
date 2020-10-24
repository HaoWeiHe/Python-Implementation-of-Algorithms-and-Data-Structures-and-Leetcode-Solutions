class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
       
        
        flag = True
        
        if (len(strs)) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
       
        min_len = len(min(strs))
        res_idx = -1
        
        for i in range(min_len):
            
            start = strs[0][i]
            for _str in range(1,len(strs)):
                
                if not (start == strs[_str][i]):
                    return strs[0][:i]
                
            res_idx = i
            
        return strs[0][:res_idx+1]
            