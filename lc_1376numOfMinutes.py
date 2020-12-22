class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        topology problem:
        start from headID
        bfs
        return the max in the tail
        """
        g = collections.defaultdict(list)
        for idx,m in enumerate(manager):
            g[m].append(idx)
        
        q = deque([(headID,0)])
        res = 0
        
        while q:
            top, t = q.popleft()
            res = max(res, t)
            
            for e in g[top]:
                q.append((e,t + informTime[top]))
        return res
                