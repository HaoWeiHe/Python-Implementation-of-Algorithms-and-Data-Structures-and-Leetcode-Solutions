class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        g = defaultdict(list)
        for a,b in tickets:
            g[a].append(b)
        for key in g:
            g[key].sort()
            
        def post_order(node):
           
            res = []
            while g[node]:
                e = g[node].pop(0)
                res+= post_order(e)
            return res + [node]
        res = post_order("JFK")
        return res[::-1] 
            