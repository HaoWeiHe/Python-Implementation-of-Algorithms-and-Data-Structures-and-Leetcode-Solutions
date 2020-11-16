class Solution(object):
    def longestSubsequence2(self, arr, difference):
        """
        using hashmap 
        """
        res = {}
        for ele in arr:
            res[ele] = res[ele - difference] +1 if ele - difference in res else 1

        return max(res.values())
    def longestSubsequence2(self, arr, difference):
        """
        dp[i] = longestSubsequence from 0 to i 
        dp[i] = max(dp[j] +1, dp[i]) for j from 0 to j 
        [1,5,7,8,5,3,4,2,1],
tmpres   1 1 1 1 2 3 
        """
        dp = [1] * len(arr)
        res = 1
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] +1)
                    res = max(res, dp[i])
        return res

