class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        def dfs(i):
            if visit[i] == -1:
                return False
            
            if visit[i] ==1:
                return True
            
            
            visit[i] = -1
            
            for node in graph[i]:
                if not dfs(node):
                    return False
                
            visit[i] = 1
            
            return True
            
        
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True
