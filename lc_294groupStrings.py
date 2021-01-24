import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)

        for ele in strings:
            pre = ord(ele[0])
            group = ""
            for c in ele:
                group += str((ord(c) - pre)%26)
                pre = ord(c)
            d[group].append(ele)
        
        return d.values()
