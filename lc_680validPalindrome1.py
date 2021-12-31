class Solution(object):
    def validPalindrome(self, s):
        """
        "abca"
         l  r
          lr  if c ==0, try l -= 1 or r += 1
         
         
         "abc"
          l r
           lr
          lr
           
        """
        def check(l,r,c):
            while l < r:
                if s[l] == s[r]:
                    l +=1
                    r -= 1
                else:
                    if c != 0:
                        return False
                    return check(l+1, r, c +1) or check(l, r-1, c+1)
            return True
        return check(0, len(s) -1, 0)
                