# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.lst = []
        def trv(root):
            if not root:
                return 
            self.lst.append(root.val)
            trv(root.right)
            trv(root.left)
        trv(root)
        
        
        
        cans = Counter(self.lst).most_common(len(self.lst))
        ans = []
        #[(2:0),(   )]
        for v, s in cans:
            if s!= cans[0][1]:
                break
            ans.append(v)
        return ans
      