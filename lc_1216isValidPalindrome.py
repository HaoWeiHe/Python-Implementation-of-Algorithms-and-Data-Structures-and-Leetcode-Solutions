class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        abcdeca
         i
            j
        """
        self.v = {}
        def dfs(i,j):
            if i == j:
                return 0
            if j - i == 1:
                return s[i] != s[j]
            
            if (i,j) in self.v:
                return self.v[(i,j)]

            if s[i] == s[j]:
                self.v[(i,j)] = dfs(i+1, j-1)
                return self.v[(i,j)]
            
            self.v[(i,j)] = 1 + min(dfs(i+1, j), dfs(i,j-1))
            return self.v[(i,j)] 
        
        return dfs(0,len(s)-1) <= k
            
                
   
    def isValidPalindrome3(self, s, k):
        """
        abcdeca
         i
            j
        """
        self.v = {}
        def dfs(i,j,k):
            if (i,j,k) in self.v:
                return self.v[(i,j,k)]
            if k < 0:
                return False
            if i >= j:
                return True
            
            while i < j:
                if s[i] != s[j]:
                    self.v[(i,j,k)] = dfs(i+1,j,k-1) or dfs(i, j-1,k-1) 
                    return self.v[(i,j,k)]
                else:           
                    i += 1
                    j -=1
            self.v[(i,j,k)] = True
            return self.v[(i,j,k)]
        return dfs(0,len(s)-1, k)
            
                
    def isValidPalindrome2(self, s, k):
        """
        abcdeca
         i
            j
        """
        def dfs(i,j,k):
            
            if k < 0:
                return False
            if i >= j:
                return True
            
            while i < j:
                if s[i] != s[j]:
                    return dfs(i+1,j,k-1) or dfs(i, j-1,k-1) 
                else:           
                    i += 1
                    j -=1
            return True
        return dfs(0,len(s)-1, k)
            
                


