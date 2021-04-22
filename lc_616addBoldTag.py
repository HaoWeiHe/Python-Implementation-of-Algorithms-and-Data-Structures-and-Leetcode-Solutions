class Solution(object):
    def addBoldTag(self, s, dict):
        """
        bold = [False, False, False]
        check i + len(w) for i in range(len(s))
        #we get bold list
        [False, True, True, False, False]
        i = 0
        1) while i is vaild, marked and update i (i ++ until False)
        2) else append(s[i]) to ans
        """
        bold = [0] * len(s)
        for w in dict:
            start = s.find(w)
            while start != -1:
                for i in range(start, start + len(w)):
                    bold[i] = 1
                start = s.find(w, start + 1)
        ans = ""
        i = 0
        while i < len(s):
            if bold[i]:
                ans += "<b>"
                while i < len(s) and bold[i]:
                    ans  = ans + s[i]

                    i += 1
                ans += "</b>"
            else:
                ans += s[i]
                i += 1
        return ans
s, dict ="abcxyz123", ["abc","123"]
print(Solution().addBoldTag(s,dict))