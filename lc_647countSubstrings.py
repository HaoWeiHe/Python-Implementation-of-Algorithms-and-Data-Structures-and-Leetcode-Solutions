class Solution(object):
    def countSubstrings(self, s):
        """
        "abc"
       i  v
       j  v
        aaa
      i v
      j   v
      if odd, cmp first
      if even, cmp first
      
      cbac
      AxxB
        """
        self.v = {}
        def isPalindromic(s):
            if s in self.v:
                return self.v[s]
            l,r = 0, len(s) -1 
            while l <r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        c = 0 
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                target = s[i:j + 1]
                
                ans = isPalindromic(target)
                self.v[target] = ans
                c += ans
                
        return c
                