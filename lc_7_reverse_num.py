class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
 
        sign = 1 if x > 0 else 0
        x = str(abs(x))[::-1]
        idx = 0
        for i,val in enumerate(x):
            idx = i
            if val != 0: break
        
        res = int(x[idx:]) if sign else -1 * int(x[idx:])
        return res if -pow(2,31)  <= res <= pow(2,31) -1 else 0
        