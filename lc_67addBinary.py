class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a, b = zfill(a,n), zfill(b,n)
        car,rem,res = 0,0,""
        for i in range(n-1,-1,-1):
            car,rem = divmod(int(a[i]) + int(b[i])+ car,2 )
            res = str(rem) + res 
            
        return "1"+ res if car else res