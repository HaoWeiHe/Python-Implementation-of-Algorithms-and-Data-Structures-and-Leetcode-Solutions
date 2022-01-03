class Solution(object):
    def customSortString(self, order, s):
        """
         "abcd"
         c:1
         b:2
         a:3
         abcd
         {1: [c], 2:[b], 3:[a]}
         [cbad]
         not in excluded [d]
         
         cbafg
         c:1
         b:2
         a:3
         f:4
         g:5
         
         abcd
         {3:[a], 2:[b], }
        """
        m, excluded = {},[]
        g = defaultdict(list)
        for i, v in enumerate(order):
            m[v] = i
        for e in s:
            if e in m:
                g[m[e]].append(e)
            else:
                excluded.append(e)
        ans = []
        for k in range(26):
            if k not in g:
                continue
            ans.extend(g[k])
        return "".join(ans + excluded)