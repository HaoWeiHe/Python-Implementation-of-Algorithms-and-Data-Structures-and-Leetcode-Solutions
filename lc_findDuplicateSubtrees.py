# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        self.res =[]
        C = collections.Counter()
        def dfs(node ):
            if not node: return ""
            uid = "L"+ dfs(node.left) + str(node.val) + "R" + dfs(node.right) 
            C[uid] += 1
            if C[uid] ==2:
                self.res.append(node)
            return uid
        dfs(root)
        return self.res