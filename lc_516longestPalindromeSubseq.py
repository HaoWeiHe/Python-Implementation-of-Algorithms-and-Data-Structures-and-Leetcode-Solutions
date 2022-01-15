class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        bbbab
        v   v 1
         vv 
          vv
         bab
         bb
        """
        self.v = {}
        def dfs(i,j):
            
            if (i,j) in self.v:
                return self.v[(i,j)]
            if  i == j :
                return 1
            if j - i == 1:
                return 2 if s[i] == s[j] else 1
            if s[i] == s[j]:
                self.v[(i,j)] = 2 + dfs(i + 1, j - 1)
            else:
                self.v[(i,j)] = max(dfs(i + 1, j), dfs(i, j - 1))   
            return self.v[(i,j)] 
        return dfs(0, len(s) - 1) 
        