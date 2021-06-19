class Solution(object):
    def reverse(self, x):
        """
        12300
          ^

        """
        sign = [1,-1][x < 0 ]
        x = str(abs(x))
        detet = 0 
        for i in range(len(x)-1, -1, -1):
            if x[i]  != 0:
                detet = i 
                break
        ans =  sign * int(x[:detet+1][::-1]) 
        return ans if -1*2**31  < ans < 2**31 -1 else 0
        
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