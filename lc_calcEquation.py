
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        g = collections.defaultdict(list)

        for i in range(len(equations)):
            a,b = equations[i]
            v = values[i]
            g[a].append((b,v))
            g[b].append((a,1.0/v))
        
        def dfs(a,target, acc,visted):
            if a not in g: return -1
            if a == target: return acc
            if a not in visted:
                return max([dfs(e,target, acc*v,visted+[a]) for e,v in g[a]])
            else:return -1
        res = []
        for query in queries:
            a,b = query
            if a == b: 
                if a in g: res.append(1)
                else: res.append(-1)
            else:
                res.append(dfs(a,b,1,[]))
            # print(res)
        return res

equations, values, queries =  [["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(Solution().calcEquation(equations, values, queries))
