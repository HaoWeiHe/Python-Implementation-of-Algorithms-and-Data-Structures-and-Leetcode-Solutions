class Solution(object):
    def convertToTitle(self, n):

        res = ""
        while n:
            digit = (n-1) % 26
            res = chr(digit + 65) + res
            n = (n-1) /  26
        return res