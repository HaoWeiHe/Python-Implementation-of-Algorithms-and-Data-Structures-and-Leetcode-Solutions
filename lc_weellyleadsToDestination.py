from collections import defaultdict, deque
class Solution(object):

    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        v  = [0] * n
        g = defaultdict(list)
        for e in edges:
            g[e[0]].append(e[1])
            
        def dfs(node):
            if len(g[node]) == 0:
                return node == destination
            if v[node] == 1:
                return False
            v[node] = 1
            ans = True
            for ele in g[node]:
                ans = ans and dfs(ele)
            v[node] = 0
            return ans
        return dfs(source)
                    
    def leadsToDestination2(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if not edges:
            return source == destination
        # if source == destination:
        #     return True

        circle = set()
        g = defaultdict(list)
        for e in edges:
            inN, outN = e
            if inN == outN:
                circle.add(inN)
                continue
            g[inN].append(outN)
        if source == destination:
            return source not in circle
        q = deque(g[source])
        v = set()
        if not q:
            return source == destination and len(g[source]) ==0
        while q:
            top = q.popleft()
            if top in circle:
                return False
            if top in v:
                continue
            if top != destination:
                v.add(top)
            end = True
            for e in g[top]:
                if e in v:
                    continue

                end = False
                q.append(e)
            
            if end:
                if top != destination:return False
        return True
