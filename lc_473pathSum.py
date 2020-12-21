# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        use prefix sum and backtracking
        """
        self.res = 0
        if not root:return 0
        
        def dfs(root,record, acc):
            if not root:return 
            acc += root.val
            if (acc - sum) in record:
                self.res += record[acc - sum]
            if acc not in record:
                record[acc] = 0 
            record[acc] +=1 
            dfs(root.right, record, acc)
            dfs(root.left, record, acc)
            record[acc] -=1
        dfs(root, {root.val:1},root.val)
        return self.res