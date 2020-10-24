class Solution(object):  
    def reverse(self, x):  
        """ 
        :type x: int 
        :rtype: int 
        """  
        res = 0  
        flag = x < 0 and -1 or 1  
        x *= flag  
        while x != 0:  
            res = res * 10 + x % 10  
            x /= 10  
        if (res > 2147483647 and flag > 0) or (res > 2147483648 and flag < 0):  
            return 0  
        return res * flag  
