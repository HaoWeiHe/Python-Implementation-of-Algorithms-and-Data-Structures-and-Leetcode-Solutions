# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        i = 0 
        #[1,2,3,4,5,N,7, None,N,N,N]
        #           v 
        while q[i]:
            q.append(q[i].left)
            q.append(q[i].right)
            i += 1
        
        return not any(q[i:])
