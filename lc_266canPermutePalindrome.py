class Solution(object):
    def canPermutePalindrome(self, s):
        """
        abba
        aba
        
        allow at most one single char
        others should be pairs
        """
        c  = collections.Counter(s)
        flag = 0
        for char, counter in c.items():
            
            if counter % 2 ==1:
                flag +=1
            if flag == 2:
                return False
        return True