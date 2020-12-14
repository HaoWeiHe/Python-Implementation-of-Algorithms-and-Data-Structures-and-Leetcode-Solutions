class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        record = {}
        wordDict =set(wordDict)
        lens = set([len(e) for e in wordDict])
        def dfs(i):
            if i == len(s):
                return True
            if i in record:
                return record[i]
            
            for lgth in lens:
                if s[i: i+lgth] in wordDict:
                    res = dfs(i+lgth)
                    record[i] = res    
                    if res:
                        return True
            return False
          
        return dfs(0)