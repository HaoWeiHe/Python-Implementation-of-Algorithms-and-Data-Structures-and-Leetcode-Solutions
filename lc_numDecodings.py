class Solution(object):
    def numDecodings(self, s):
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
