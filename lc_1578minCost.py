
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        res, maxcost = 0, 0
        for idx, val in enumerate(s):
            if idx > 0 and s[idx] != s[idx-1]:
                maxcost = 0
            res += min(maxcost, cost[idx])
            maxcost = max(maxcost, cost[idx])
        return res
            
    def minCost2(self, s, cost):
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
        