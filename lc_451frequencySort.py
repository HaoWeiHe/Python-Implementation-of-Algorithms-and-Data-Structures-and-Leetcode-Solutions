class Solution(object):
    def frequencySort(self, s):
        """
        {e:2, t:1, r:1}
        [(e,2),(t,1),(r,1)]
        """
        c = Counter(s)
        lst = sorted(c.items(),key= lambda (x,v):v, reverse = True)
        return "".join([e*c[e] for e,_ in lst]) #(e,2)
        