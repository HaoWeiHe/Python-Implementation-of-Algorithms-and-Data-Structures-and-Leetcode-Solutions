

class Solution(object):
    def getImportance(self, employees, id):
        """
        use bfs, +val until subordinates is null 
        """
       #d[id]: employees
        ans = 0
        g ={}
        for e in employees:
            g[e.id] = e
        q = deque([id])
        while q:
            top = q.popleft()
            ans += g[top].importance
            q += g[top].subordinates
        return ans
                    
        