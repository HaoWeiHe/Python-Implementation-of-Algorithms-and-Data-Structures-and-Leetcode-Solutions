# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        self.interval = inorder(root)
        print(self.interval)
        self.idx = 0
        

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.interval[self.idx-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        
        return self.idx < len(self.interval)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()