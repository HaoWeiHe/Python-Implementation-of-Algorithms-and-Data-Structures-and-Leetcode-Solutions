# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return 
        q = deque([(root,0)])
        res = []
        while q:
            node, lvl = q.popleft()
            if not node: continue
            if lvl == len(res):
                res.append([])
            res[lvl] += [node.val]
           
            q.append((node.left, lvl + 1))
            q.append((node.right, lvl + 1))
            
        return res
            