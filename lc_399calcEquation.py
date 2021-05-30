from collections import defaultdict, deque
class Solution(object):
    def calcEquation(self, equations, vs, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g  = defaultdict(list)
        for i, v in enumerate(equations):
            f, t = v
            g[f].append((t, vs[i]))
            g[t].append((f, 1.0/vs[i]))
        
        def bfs(f,t):
            q = deque([(f,1)])
            visted = set()
            
            while q:
                e = q.popleft()
                top, v = e
                if top in visted:
                    continue
                visted.add(top)
                for e in g[top]:
                    node, value = e
                    if node == t:
                        return v * value
                    q.append((node, v * value))
            return -1
        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
            
        return  res

a,b,c = [["a","b"],["b","c"]],  [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(a,b,c))