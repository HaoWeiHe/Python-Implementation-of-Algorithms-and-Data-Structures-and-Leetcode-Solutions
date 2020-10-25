
class Solution(object):
    def numDecodings(self, s):

        if not s: 
            return 0

        dp1, dp2 = 1 , 1 if s[0] != "0" else 0
 
        
        for i in range(2, len(s)+1):
            tmp = 0

            if s[i-1] != "0":
                tmp = dp2

            two_digital = int(s[i-2:i])
            if 10 <=  two_digital <= 26:
                tmp += dp1
            dp2, dp1 = tmp, dp2
        return dp2

    def numDecodings2(self, s):

        if not s: 
            return 0

        dp = [0 for _ in range(len(s)+1)]
        dp[0], dp[1] = 1 , 1 if s[0] != "0" else 0

        for i in range(2, len(s)+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1] 
            
            two_digital = int(s[i-2:i])
            if 10 <=  two_digital <= 26:
                dp[i] += dp[i-2]

        return dp[-1]

        

    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0
        self.memo = {}

        def dfs(i):
            if i > len(s): return 
            if i == len(s): 
                self.res += 1
                return 

            if i in self.memo:
                self.res += self.memo[i]
                return  
            if s[i] == '0': 
                return 

            dfs(i+1)

            if 1 <= int(s[i:i+2]) <= 26:
                dfs(i+2)

            self.memo[i] = self.res

        dfs(0)

        return self.res
