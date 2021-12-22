class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        degree = defaultdict(int)
        conn  = defaultdict(set)
        
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
            if a < b:
                conn[a].add(b)
            else:
                conn[b].add(a)
        
        res = float('inf')
        for i in range(1, n + 1):
            for j in conn[i]:
                for k in conn[i].intersection(conn[j]):
                    res = min(res, degree[i] + degree[j] + degree[k] - 6)
        return -1 if res == float('inf') else res
                
            
    def minTrioDegree2(self, n, edges):
        ## key is node, value is degree(number of connected edges)
        degree_count = {key: 0 for key in range(1, n + 1)}
        
        res = float('inf')
        ## set of nodes connected to the key node
        connections = {key: set() for key in range(1, n + 1)}
        
        for a,b in edges:
            degree_count[a] += 1
            degree_count[b] += 1
            
            if a < b:
                connections[a].add(b)
            else:
                connections[b].add(a)
        
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if j not in connections[i]:
                    continue
                
                for k in connections[j]:
                    if k in connections[i]:
                        res = min(res, degree_count[i] + degree_count[j] + degree_count[k] - 6)
                        
        return res if res != float('inf') else -1

# class UnionFind():
#     def __init__(self, n):
#         self.parent = [ele for ele in range(n)]
#         self.rank = [0] * n
        
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self,x, y):
#         x, y = x - 1, y - 1
#         px, py = self.find(x), self.find(y)
#         if px == py:
#             return True
#         if self.rank[px] > self.rank[py]:
#             self.parent[py] = px
#         elif self.rank[py] <  self.rank[px]:
#             self.parent[py] = px
#         else:
#             self.parent[py] = px
#             self.rank[px] += 1
#         return False
    
# class Solution(object):
#     def minTrioDegree(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: int
#         """
#         trios = []
#         degree = defaultdict(set)
#         uf = UnionFind(n)
#         for a,b in edges:
#             degree[a].add(b)
#             degree[b].add(a)
#             tmp = []
#             if uf.union(a,b):
#                 for c in degree[b].intersection(degree[a]):
#                     trios.extend([[a,b,c]])
#                     tmp.append(c)
#                 # trios.extend([[a,b,c] for c in degree[b].intersection(degree[a])])
                
#             for c in tmp:
#                 degree[b].remove(c)
#                 degree[c].remove(c)
#         ans = float('inf')

#         for t in trios:
#             ans = min(ans, sum([abs(len(degree[e]) - 2) for e in t]))
                
#         return  -1 if ans == float('inf')  else ans
        
#         