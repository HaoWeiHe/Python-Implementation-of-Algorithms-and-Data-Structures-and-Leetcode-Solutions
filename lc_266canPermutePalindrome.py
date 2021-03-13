class Solution(object):
    def canPermutePalindrome(self, s):
        """
        alp is paired, can have at most one unpair
        """
        c = Counter(s)
        up = 0
        for i in c.values():
            if i%2 != 0:up+=1
            if up > 1:return False
        return True
        