# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:return[]
        boundary = [root.val]

        def dfs(root):
            if not root: return 
            if not root.right and not root.left:return 
            boundary.append(root.val)
            if not root.left :
                dfs(root.right)
            else:
            # lf.append(root.val)
                dfs(root.left)
        

        def h3(node):
            if not node: return 
            if node != root and not node.right and not node.left: boundary.append(node.val) 
            h3(node.left)
            
            h3(node.right)
        

        def dfsrt(root):
            if not root or not root.right and not root.left: return 
            
            if not root.right :
                # rt.append(root.val)
                dfsrt(root.left)
            else:
                dfsrt(root.right)
            boundary.append(root.val)
        
        
        
        dfs(root.left)
        h3(root)
        dfsrt(root.right)
        return boundary