
class Solution(object):
    def nextGreaterElement(self, s):
        digits = list(str(s))
        n = len(digits)
        i = n - 1
        while i >= 0 and digits[i-1] >= digits[i]:
            i -= 1

        if i == -1:
            return -1
        
        j = i 
        while j  < len(digits) and  digits[j] > digits[i-1]:
            j += 1
        j -= 1  
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        ans = int(''.join(digits)) 

        return ans if ans < 1 << 31 else -1