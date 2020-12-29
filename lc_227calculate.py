class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, lastNum, res = 0,0,0
        op = "+"
        s = s.replace(" ","")
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if i == len(s) -1 or not c.isdigit():
                if op == "+":
                    res += lastNum
                    lastNum = num
                if op == "-":
                    res += lastNum
                    lastNum = -num
                if op == "*":
                    lastNum = lastNum * num
                if op == "/":
                    lastNum = int(float(lastNum)/ num)
                op = c
                num = 0
        res += lastNum
        return res

