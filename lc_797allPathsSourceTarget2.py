class Solution(object):
    def allPathsSourceTarget(self, graph):
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