# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(start, end):
            if start > end:
                return None
            
            mid = (start + end)/ 2
            node = TreeNode(nums[mid])
            
            node.left = dfs(start, mid -1)
            node.right = dfs(mid +1, end)
            return node
        
        return dfs(0, len(nums) -1)
        
            
        