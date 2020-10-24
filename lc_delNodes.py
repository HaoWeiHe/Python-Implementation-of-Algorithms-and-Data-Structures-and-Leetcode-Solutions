
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def dfs(node, parent_exist = False):
            if not node: return None
            
            if node.val not in to_delete:
                if not parent_exist: res.append(node)
                node.left = dfs(node.left, 1)
                node.right = dfs(node.right, 1)
                return node
            else:
                node.left  = dfs(node.left, False)
                node.right = dfs(node.right, False)
                return None
        dfs(root)
        return res

