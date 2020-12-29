class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def helper(l,r):
            while l < r:
                if s[l]!= s[r]:
                    return False,l,r
                l +=1 
                r -= 1
            return True, None, None
        
        res, l, r = helper(0,len(s)-1)
        if res: return True
        return helper(l,r-1)[0] or helper(l+1,r)[0]
