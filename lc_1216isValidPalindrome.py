class Solution(object):
    def isValidPalindrome(self, s, k):
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
            
                