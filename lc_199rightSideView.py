# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        
        """
        if not root:return []
        res =[]
        q = deque([(0,root)])
        while q:
            level, node = q.popleft()
            if node.left:
                q.append((level+1,node.left))
            if node.right:
                q.append((level+1,node.right))
           
            if len(res) == level:
                res.append(node.val)
            else:
                res[level] = node.val
        return res
            