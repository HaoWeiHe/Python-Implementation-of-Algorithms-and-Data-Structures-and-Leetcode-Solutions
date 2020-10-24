

class Solution(object):
    def isBipartite(self, graph):
        colored = dict()
        def helper(start):
            q = [(start, 1)]
            while (q):
                top, color = q.pop(0)
                # print(q)
                if top in colored :
                    if colored[top]!=color: 
                    
                        return False
                    # print(top)
                    continue
                colored[top] = color
                for e in graph[top]:
                    q.append((e,-color))
            return True


                
        for vertex ,links in enumerate(graph):
            if vertex in colored: continue
            if  helper(vertex) ==False: 
                    return False
            
        return True
# 0-1
#    |
# 2- 3
graph =[[1],[0,3],[3],[1,2]]
print(Solution().isBipartite(graph))