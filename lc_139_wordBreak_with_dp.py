class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        LEETCODE
        LEET | CODE
            j     i
        dp[i]: wordBreak(s[0->i])
        dp[i] = any(dp[j] && s[j:i] is a word)
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict :
                    dp[i] = True
                    break
        return dp[-1]