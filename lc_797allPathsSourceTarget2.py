from collections import deque
class Solution(object):
    def allPathsSourceTarget(self, graph):
        q = deque([(0,[0])])
        res =[]
        while q:
            top, his = q.popleft()
            if top == len(graph) -1:
                res.append(his)
                continue   
            for e in graph[top]:
                q.append((e, his + [e]))
        return res
    def allPathsSourceTarget2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(node,his):
            if node == len(graph) -1 :
                self.res.append(his)
                return
            for e in graph[node]:
                dfs(e, his +[e])
        dfs(0, [0])
        return self.res