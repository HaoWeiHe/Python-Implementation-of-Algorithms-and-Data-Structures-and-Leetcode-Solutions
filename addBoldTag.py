class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bold = [0 for _ in range(len(s))]
        dic = collections.defaultdict(set)
        for ele in dict:
            dic[len(ele)].add(ele)
        

        for i in range(len(s)):
            for length, sets in dic.items():
                if "".join(s[i:i+length]) in sets:
                    bold[i:i+length]  = [1]*length
                # lenght = len(ele)
                # if "".join(s[i : i+lenght]) == ele:
                #     bold[i:i+lenght] = [1]* lenght
        res = ""
        #Begin:[,..0,1,..], [1,..]
        #end:[..,1,0] , [1,1,1]
        flag_0, flag_1 = False, False
        for idx, val in enumerate(bold):
            if idx ==0 and val ==1: 
                res += "<b>"
            if flag_0 and val ==1: 
                res += "<b>"
            if flag_1 and val ==0:
                res += "</b>"
            res += s[idx]
            if idx == len(s)-1 and val == 1:
                res += "</b>"

            flag_0 = val == 0
            flag_1 = val ==1
        return res
