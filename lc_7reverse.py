class Solution(object):
    def reverse(self, x):
        """
        123
         ^
        tmp 3   2 1 
        res 12  1 0
        
        ans = 0
        ans *10 + 3 = 3
        32
        
        """
        mx =  2**31 -1 
        
        sign = [-1,1][x > 0]

        x = abs(x)
        res = 0 

        while x:
            mod = x % 10
            if sign == 1:
                if res > mx/ 10 or (res == mx/10 and mod > 7):
                    return 0
            else:
                if res > mx/ 10 or (res == mx/10 and mod > 8):
                    return 0
            res = res*10 + mod
            x /= 10
        return sign* res 
class Solution(object):
    def reverse(self, x):
        """
        123
         ^
        tmp 3   2 1 
        res 12  1 0
        
        ans = 0
        ans *10 + 3 = 3
        32
        
        """
        mx =  2**31 -1 
        
        sign = [-1,1][x > 0]

        x = abs(x)
        res = 0 

        while x:
            mod = x % 10
            if sign == 1:
                if res > mx/ 10 or (res == mx/10 and mod > 7):
                    return 0
            else:
                if res > mx/ 10 or (res == mx/10 and mod > 8):
                    return 0
            res = res*10 + mod
            x /= 10
        return sign* res 

    def reverse2(self, x):
        """
        123
         ^
        tmp 3   2 1 
        res 12  1 0
        
        ans = 0
        ans *10 + 3 = 3
        32
        
        """
        mx =  2**31 -1 
        
        if x < -1*2**31 or x >= mx:
            return 0

        neg = x < 0
        x = abs(x)
        res = 0 
        while x:
            res = res*10 + x%10
            x /= 10
            if res > mx :
                return 0
        return -1* res if neg else res
print(Solution().reverse(-123))