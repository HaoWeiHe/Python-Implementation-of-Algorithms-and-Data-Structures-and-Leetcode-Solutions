class Solution(object):
    def romanToInt(self, s):
        """
        Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

ans = 0
MCMXCIV 
   v
*MC inv
M, ans = 1000
CM (C<M) valid,
ans = 1000 + (M-C) = 1900
XC (X < C), valid
keep going
        """
        ans = 0 
        i = 0
        d = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        while i < len(s):
            if i == len(s)-1:
                ans += d[s[i]]
                break
            if d[s[i]] < d[s[i+1]]:
                ans += (d[s[i+1]] - d[s[i]])   
                i += 2
                
            else:
                ans += d[s[i]]
                i += 1
            
            
        return ans
            