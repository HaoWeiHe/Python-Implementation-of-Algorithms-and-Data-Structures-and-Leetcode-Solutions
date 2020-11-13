class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        mins = {
            "V":"I",
            "X":"I",
            "L":"X",
            "C":"X",
            "M":"C",
            "D":"C"
            
        }
        if not s:
            return 0
        pre = s[0]
        acc = 0
        for e in s:
            if e in mins and mins[e] == pre:
                acc += (values[e] -2*values[pre] )
            else:
                acc += values[e]
            pre = e
        return acc