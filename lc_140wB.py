class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        "dog cats and"
         dog cat sand
        """
        self.d = {}

        def dfs(s):

            if not s: 
                return [""]
            
            lst =[]
            if s in self.d:
                return self.d[s]

            for w in wordDict:
                if s[:len(w)] != w: 
                    continue    
                for e in dfs(s[len(w):]):
                    if e:
                        lst.append(w + " " + e)
                    else:
                        lst.append(w)

            self.d[s] = lst
            return lst
                    
        return dfs(s)



s =  "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s,wordDict))