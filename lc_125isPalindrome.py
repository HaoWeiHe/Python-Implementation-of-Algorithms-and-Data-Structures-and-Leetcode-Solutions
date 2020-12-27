class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0 , len(s)-1
        while l < r:
            while not ( s[l].isalnum() ) and l < r :
                l +=1
            while  not ( s[r].isalnum() )  and l < r :
                r -=1
            
            if s[r].lower()!=s[l].lower():
                return False
            l +=1
            r -=1
        return True
