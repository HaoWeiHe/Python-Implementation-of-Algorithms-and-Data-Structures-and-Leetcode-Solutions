# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and dfs(t1.right, t2.left) and dfs(t1.left, t2.right)
        return dfs(root, root)
        
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque([root])
        while q:
            tmp_len = len(q)
            tmp = []
            for _ in range(tmp_len):
                top = q.popleft()
                if top:
                    tmp.append(top.val)
                else:
                    tmp.append(None)
               
                if not top:
                    continue
                q.append(top.right)
                q.append(top.left)
            l, r = 0, len(tmp)-1
           
            while l < r:
                if tmp[l] != tmp[r]:
                    return  False
                l += 1
                r -= 1
        return True

