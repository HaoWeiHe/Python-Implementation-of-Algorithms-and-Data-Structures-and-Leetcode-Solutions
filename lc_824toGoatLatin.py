class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = S.split(" ")
        res = []
        for idx,e in enumerate(s):
            if e[0].lower() not in ["a","e","i","o","u"]:
                e = e[1:] + e[0]
            e += "ma"
            e += "a"*(idx+1)
 
            res.append(e)
        return ' '.join(res)