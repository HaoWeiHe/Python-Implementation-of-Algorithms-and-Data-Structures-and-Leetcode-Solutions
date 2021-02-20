class Solution(object):
    def longestPalindrome(self, s):
        """
        bab
         v
        3/2 = 1
        1-1, 1+1
        bb
        2/2 = 1
        """
        def p(cur):
            res,tmp =  "", 0 
           	
            def f(tmp, i,j):
            	
                while i >= 0 and j < len(s) :
                    if s[i]!=s[j]:break
                    i -= 1
                    j += 1
                    tmp+= 2

                return s[i+1:j]
            
            re = f(0, cur, cur + 1)
            if len(re) > len(res):
                res = re
                
            re = f(1,cur-1, cur + 1)
            
            if len(re) > len(res):
                res = re
            
            return res
        
        res = ""
        for cur in range(len(s)):
            now = p(cur)
            if len(res) < len(now):
                res = now
        return res

# s = "cbbd"
# print(Solution().longestPalindrome(s))