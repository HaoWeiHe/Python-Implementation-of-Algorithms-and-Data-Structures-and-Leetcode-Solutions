# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res =[]
        def dfs(root, record, acc):
            if not root:
                return 
            
            record.append(root.val)
            acc += root.val
            if not root.right and not root.left:
                if acc == sum:
                    self.res.append(record[:])
                record.pop()
                return 
            
            dfs(root.right, record, acc)
            dfs(root.left,  record, acc)
            record.pop()

        dfs(root, [],0)
        return self.res
        