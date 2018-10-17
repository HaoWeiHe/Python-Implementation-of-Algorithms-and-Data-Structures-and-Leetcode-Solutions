class Solution(object):
    
    def __init__(self):
        self.res = ""
        
    def longestPalindrome(self, s):
        
        evenFlag = True if not len(s)%2 else False
        
        if len(s) < 2 :
            return s
        
        for i in range(len(s)-1):
            self.getLPD(i,i+1,s)
            self.getLPD(i,i,s)
            
        return self.res
    
    def getLPD(self,start, end, s ):
        
        while(start >= 0 and end < len(s) and s[start] == s[end]):
            start -=1
            end  +=1
            
        if (end-start-1) > len(self.res):  
            self.res = s[start+1 : end]
