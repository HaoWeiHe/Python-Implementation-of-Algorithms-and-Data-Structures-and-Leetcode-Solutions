class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        for i in range(len(s)-1, -1, -1):
            w = s[i]
            if not w:
                continue
            return len(w)