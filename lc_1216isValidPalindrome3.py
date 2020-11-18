
class Solution(object):
    def isValidPalindrome(self, s, k):
        l, r = 0, len(s)-1
        self.mem = {}

        def check(l,r):
          
            if l >=r :
                return 0

            if (l,r) in self.mem:
                return self.mem[(l,r)]
            
            if s[l] != s[r]:
                self.mem[(l,r)] = min(check(l+1,r) +1,
                                      check(l,r-1) +1
                                      )
            else: 
                self.mem[(l,r)] = check(l+1, r-1)
            
            return self.mem[(l,r)] 
        return check(l,r) <= k
    def isValidPalindrome2(self, s, k):
        """
        if s[l]!=s[r]:
            check(l+1,r,k-1) or 
            check(l,r-1,k-1) or 
            check(l+1, r-1, k-2)
        eg.   
            "zbcdec"

            "zbcde" k = 1
            "bcdec" k = 1
            "bcde" k = 0
        """

        l, r = 0, len(s)-1
        self.mem = {}
        def isPalindrome(l,r):
            while l <=r:
                if s[l]!=s[r]:
                    return False
                l +=1
                r -=1
            return True
        
        def check(l,r,k):
            if (l,r,k) in self.mem:
                return self.mem[(l,r,k)]
            if k == 0 :
                return isPalindrome(l,r)
            if k < 0:
                return False
            while l <= r:
                if s[l]!=s[r]:
                    self.mem[l,r,k] = check(l+1,r, k-1) or  check(l,r-1,k-1) or check(l+1,r-1,k-2)
                    return self.mem[l,r,k]
                else:
                    l += 1
                    r -= 1
            return True
        return check(l,r,k)

s,k = 'baaaabaa',3
print(Solution().isValidPalindrome(s,k))