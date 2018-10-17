class Solution(object):
    def isPalindrome(self, x):
        
        if str(x)[0]=='-':
            return False
        x=str(x)
        x_length=len(x)-1
        
        
        for i in range(0,x_length):
            if not x[i]==x[x_length-i]:
                return False
        return True