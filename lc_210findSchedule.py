class Solution(object):
    def findOrder(self, n, prerequisites):
        inde = collections.defaultdict(int)
        g = collections.defaultdict(list)
        for a,b in prerequisites:
            inde[a] += 1
            g[b].append(a)
        res = []
        q = deque([e for e in range(n) if e not in inde])
       
   
        for i in range(n):
            while q:
                top = q.popleft()
                res.append(top)

                for e in g[top]:

                    inde[e] -= 1
                    if inde[e] == 0:
                        q.append(e)
                   
       
        if len(res)!= n:
            return ""
        return res