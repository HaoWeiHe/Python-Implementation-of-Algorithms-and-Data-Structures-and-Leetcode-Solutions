class Solution(object):
    def minCost(self, s, cost):
        """
         "abaac"
              l 
               r
        """
        l,r = 0,0
        ans = 0
        
        while l < len(s):
            while r < len(s) and s[r] == s[l]:
                r += 1
            if r-l > 1:
                ans += sum(cost[l:r]) - max(cost[l:r])
                l = r
            else:
                l += 1
        return ans
        