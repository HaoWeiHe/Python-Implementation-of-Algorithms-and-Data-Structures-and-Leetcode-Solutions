class Solution(object):
    def strStr(self, haystack, needle):
        """
        hello
        01234
           ll
           5-2 = 3
        """
        if not needle :return 0
        n = len(needle)
        for i in range(len(haystack) - n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
        