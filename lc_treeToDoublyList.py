

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type node: Node
        :rtype: Node
        """
        self.last, self.first = None, None
        def dfs(node):
            if not node: return 
            dfs(node.left)
            if not self.first: self.first = node
            if self.last:
                self.last.right = node
                node.left = self.last
            self.last = node

            dfs(node.right)
        if not root: return None
        dfs(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first