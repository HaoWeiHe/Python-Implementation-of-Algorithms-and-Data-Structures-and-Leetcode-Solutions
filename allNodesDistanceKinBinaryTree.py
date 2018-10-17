# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        graph = dict()
        
        def dfs(node):
            
            if node not in graph :
                graph[node] = []
            
            if node.left:
                if node.left not in graph :
                    graph[node.left] = []
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)
            if node.right:
                if node.right not in graph :
                    graph[node.right] = []
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)

        dfs(root)

        visit = []
        res = []


        def bfs(node,d):
            if d < K:
                visit.append(node)
                for v in graph[node]:
                    if v not in visit:
                        bfs(v, d+1)
            else:
                res.append(node.val)

        bfs(target, 0)
        return res