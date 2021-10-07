"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.v = {}
        def traverse(root):
            if not root : 
                return root
            if root in self.v:
                return self.v[root]
            
            c_node = Node(root.val)
            self.v[root] = c_node
            for nei in root.neighbors:
                c_node.neighbors.append(traverse(nei))
            return c_node
        return traverse(node)
        
        