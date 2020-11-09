class Solution(object):
    def validPalindrome(self, s):
        """
        1. use two pointer to check if the location of pointer r and l is equal or not 
        2. if not equal, check the strings without cur position, 
    
        """
        
        n = len(s)
        right, left = 0, n - 1
        
        while right <= left:
            if s[right] == s[left]:
                right +=1
                left -=1
            else:
                string2 = s[:left] + s[left+1:]
                string1 = s[:right] + s[right+1:]
                return string2 == string2[::-1] or string1 == string1[::-1]
        return True
            
        
