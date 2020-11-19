
class Solution(object):
    def isMatch(self, s, p):
        """
        dp[i][j] = 
                dp[i-1][j-1]  # if  same or "."
                dp[i][j-2]    #if p_cur == "*" and empty
                dp[i][j-1]    #if p_cur == "*" and single a
                dp[i-1][j]    #if p_cur == "*" and muliple a
                false         #non of above
        """
      
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
   
        for i in range(len(p)):
            if p[i] =="*":
                dp[0][i+1] = dp[0][i-1]

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or  p[j] ==".":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    dp[i+1][j+1] = dp[i+1][j-1]
                    if s[i] == p[j-1] or p[j-1] == ".":
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i+1][j+1]
                        
        return dp[-1][-1]
     

test_cases = [("aa","a"),( "aa","a*"),( "ab", ".*"),( "aab", "c*a*b"), ("mississippi", "mis*is*p*.")]
ans = [False, True, True, True, False]

sol = Solution()
for idx, val in enumerate(test_cases):
    print("my_ans: {}\t true_ans:{}\t{} ".format(sol.isMatch(val[0],val[1]),ans[idx], ans[idx] ==sol.isMatch(val[0],val[1]) ))

