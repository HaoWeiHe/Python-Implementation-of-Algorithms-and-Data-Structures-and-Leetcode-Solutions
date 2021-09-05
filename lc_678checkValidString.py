
class Solution(object):
    def checkValidString(self, s):

        lo, hi = 0, 0
        for e in s:
            if e == "(":
                lo, hi = lo + 1, hi + 1
            if e == ")":
                lo, hi = lo - 1, hi - 1
            if e == "*":
                lo, hi = lo - 1, hi + 1
            if hi < 0  :
                return 0
            lo = max(lo,0)
      
        return lo <=0 <= hi
    def checkValidString2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dfs(i, c):
            if i == len(s):
                return c == 0
           
            if s[i] == "(":
                return dfs(i+1, c+1)
            
            if s[i]  == ")":
                if c == 0:
                    return False
                return dfs(i+1, c-1)
           
            return dfs(i+1,c) or dfs(i+1, c+1) or dfs(i+1, c-1)
        return dfs(0,0)
                
                