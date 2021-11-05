class Solution(object):
    def isSubsequence(self, s, t):
        """
        abcde
            v
        ace
          i
        """

        i = 0 
        for cur in t:
            if i >= len(s):
                break
            if cur == s[i]:
                i += 1
            
        return True if i == len(s) else False