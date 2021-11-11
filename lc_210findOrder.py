from heapq import heappush, heappop

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = {}
        outdegres = collections.defaultdict(list)
        for c in range(numCourses):
            indegree[c] = 0 
        
        for a,b in prerequisites:
            indegree[a] += 1
            outdegres[b].append(a)
        q = deque([ele for ele in indegree if indegree[ele] == 0 ])
        ans = []
        
        v = set()
        while q:
            top = q.popleft()
            if top in v:
                continue
            ans.append(top)
            v.add(top)
            for e  in outdegres[top]:
                indegree[e] -= 1
                if indegree[e] == 0:
                    q.append(e)
                        
     
        return ans if len(ans) == numCourses else []
        
        
        