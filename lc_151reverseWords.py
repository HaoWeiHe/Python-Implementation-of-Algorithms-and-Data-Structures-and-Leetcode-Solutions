class Solution(object):
    def reverseWords(self, s):
        """
        "the sky is blue"
        "  "
        """
        s = s.split(" ")
        res = []
        for e in s:
            if e!="":
                res.append(e)
        
        
        return " ".join(res[::-1])
