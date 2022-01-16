# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        
        val, lvl = q.popleft()
        if lvl < len(ans):
            ans.append()
        else:
            cmp ans[steps] and val
            
        ans []
        """
        if not root:
            return []
        ans = []
        q = deque([(root,0)])
        while q:
            node, lvl = q.popleft()
            if not node:
                continue
            if lvl == len(ans):
                ans.append(node.val)
    
            ans[lvl] = max(ans[lvl], node.val)
            q.append((node.right, lvl + 1))
            q.append((node.left, lvl + 1))
        return ans
        