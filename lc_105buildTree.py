# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        getinorderidx = {val:idx for idx, val in enumerate(inorder)}
     
        def helper(l,r):
            if l == r:
                return None
            nonlocal pre_idx
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            idx = getinorderidx[root_val]
            pre_idx +=1
            root.left = helper(l,idx)
            root.right = helper(idx+1, r) 
            return root
        pre_idx= 0
        return helper(0,len(preorder))