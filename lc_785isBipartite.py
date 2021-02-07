
import collections
class Solution(object):
    def isBipartite(self, graph):
        """
        [[1,3],[0,2],[1,3],[0,2]]
        """
        d = {}
        seen = set()
        if not graph:
            return True

        for idx in range(len(graph)):
            if idx not in d:
                q = collections.deque([(idx,1)])
                while q:     
                    cur, group = q.popleft()
                    for e in graph[cur]:
                        if e in d and d[e]!= group *-1:
                            return False
                        d[e] = group * -1
                        if e not in seen:
                            q.append((e, group *-1))
                    seen.add(cur)
        return True

                    
