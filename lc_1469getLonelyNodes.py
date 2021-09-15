# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = deque([root])
        res = []
        while q:
            top = q.popleft()
            if top.left and top.right:
                q.append(top.left)
                q.append(top.right)
            elif top.left:
                res.append(top.left.val)
                q.append(top.left)
            elif  top.right:
                res.append( top.right.val)
                q.append(top.right)
        return res