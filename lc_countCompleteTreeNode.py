# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        def tree_height(node):
            count=0
            while node:
                count=count+1
                node=node.left
            return count
        ans=0
    
        while root:
            left=tree_height(root.left)
            if left==tree_height(root.right):
                ans+=(1<<left)
                root=root.right
            else:
                ans+=(1<<left-1)
                root=root.left
        return ans
 