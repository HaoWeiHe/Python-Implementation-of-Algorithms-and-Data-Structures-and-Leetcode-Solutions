class Solution(object):
    def firstUniqChar(self, s):
        """
        {l:0, e:1, t:3, c:4, o:5, d:6}
        {l:4,o:9,v:2,e:11,6:7, c:8, d:10}
        """
        d = defaultdict(list)
        for i, v in enumerate(s):
            d[v].append(i)
        
        for i, v in enumerate(s):
            if i == d[v][-1] and len(d[v]) == 1:
                return i
        return -1