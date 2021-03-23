# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return 
        q = deque([(root, 0)])
        d = collections.defaultdict(list)
        while q:
            top, lvl = q.popleft()
            d[lvl].append(top.val)
            if top:
                if top.left:
                    q.append((top.left, lvl + 1))
                if top.right:
                    q.append((top.right, lvl + 1))

    
        ans = []
        for i in range(len(d)):
            if i %2 == 1:
                ans.append(d[i][::-1])
            else:
                ans.append(d[i])
        return ans