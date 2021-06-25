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
