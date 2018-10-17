class Solution(object):
    def __init__(self):
        self.res = 0
        
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def helper(right, left, res):
            while(right>=0 and left < len(s) and s[right] == s[left]):
                right -=1
                left +=1
                self.res +=1

        
        
        for idx in range(len(s)):
            helper(idx, idx, self.res)
            helper(idx, idx+1,self.res)
            
        return self.res
    
            
        
 