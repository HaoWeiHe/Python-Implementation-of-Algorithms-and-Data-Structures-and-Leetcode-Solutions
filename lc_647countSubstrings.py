class Solution():

  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0 
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    
    for i in range(n-1,-1,-1):
      for j in range(i, n):
        if s[i] == s[j] and ( j-i < 2 or dp[i+1][j-1]):
          dp[i][j] = 1
          ans += 1


    return ans
        
  def countSubstrings2(self, s):
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

print(Solution().countSubstrings("aaa"))