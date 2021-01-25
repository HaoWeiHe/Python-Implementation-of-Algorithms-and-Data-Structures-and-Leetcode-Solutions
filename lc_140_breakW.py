class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.mem = {}

        def dfs(s):
            if not s:
                return [""]
            if s in self.mem: 
                return self.mem[s]

            res = []

            for w in wordDict:
                if s[:len(w)] != w:
                    continue
                for e in dfs(s[len(w):]):
                    if r:
                        res.append(w + " " + e)
                    else:
                        res.append(w)
            self.mem[s] = res
            return res
        return dfs(s)
                    