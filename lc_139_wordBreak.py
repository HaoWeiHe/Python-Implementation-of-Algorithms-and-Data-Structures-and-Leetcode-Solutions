class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        lens = set([len(e) for e in wordDict ])
        self.res = 0
        memo = {}
        def dfs(i):
            if i == len(s):
                self.res = 1
                return 1
            if i in memo: 
                return memo[i]
            for l in lens:
                if s[i:i+l] in wordDict:
                    if dfs(i+l):
                        memo[i] = 1
                    else:
                        memo[i] = 0

        dfs(0)
        return self.res
            