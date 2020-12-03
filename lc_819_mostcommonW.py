import collections,re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        s = re.findall(r"[\w']+", paragraph)#paragraph.split("")

        s = [ele.strip("!?',;.").lower() for ele in s]
      	
        c = collections.Counter(s)
    
       
        for ele in c.most_common(len(c)):
           
            if ele[0] not in banned:
                return ele[0]
